'''
Author: TDK 793065367@qq.com
Date: 2023-11-14 00:00:01
LastEditors: TDK 793065367@qq.com
LastEditTime: 2023-11-14 10:58:57
FilePath: /My-Leetcode/daily/2023.11/1334.find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
日期: 2023-11-14
题目: 阈值距离内邻居最少的城市
链接: https://leetcode-cn.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
"""

from typing import *
from collections import *
import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        ans = [float("inf"), -1]
        map = defaultdict(list)
        for f, t, w in edges:
            map[f].append((t, w))
            map[t].append((f, w))

        for i in range(n):
            q = []
            heapq.heapify(q)
            visited = set()
            heapq.heappush(q, (0, i))


            while q:
                distance, start = heapq.heappop(q)
                if start in visited:
                    continue
                visited.add(start)
                for nxt, weight in map[start]:
                    if nxt not in visited and distance + weight <= distanceThreshold:
                        heapq.heappush(q, (distance + weight, nxt))
                        
            
            if len(visited) <= ans[0] and i > ans[1]:
                ans = [len(visited), i]
        
        return ans[1]


print(Solution().findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))