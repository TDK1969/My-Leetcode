"""
日期: 2023-10-21
题目: 统计无向图中无法互相到达点对数
链接: https://leetcode-cn.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
"""

from typing import *
from collections import *
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        groups = []
        visited = set()

        map = defaultdict(list)
        for a, b in edges:
            map[a].append(b)
            map[b].append(a)
        
        for i in range(n):
            if i not in visited:
                q = [i]
                visited.add(i)
                cnt = 1
                while q:
                    t = q.pop()
                    for nxt in map[t]:
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
                            cnt += 1
                groups.append(cnt)
        
        s = sum(groups)
        return sum(k * (s - k) for k in groups) // 2
                            
test = Solution()
print(test.countPairs(7, [[0,2],[0,5],[2,4],[1,6],[5,4]]))