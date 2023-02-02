"""
日期: 2023-02-02
题目: 颜色交替的最短路径
链接: https://leetcode-cn.com/problems/shortest-path-with-alternating-colors/
"""

from typing import *
from collections import *
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1] * n
        # 0 - red; 1 - blue
        path = [[float("inf")] * n, [float("inf")] * n]

        path[0][0] = path[1][0] = 0

        color_map = [defaultdict(list), defaultdict(list)]

        for s, e in redEdges:
            color_map[0][s].append(e)
        
        for s, e in blueEdges:
            color_map[1][s].append(e)

        q = deque()
        # (node, red/blue, distance)
        q.append((0, 0, 0))
        q.append((0, 1, 0))

        while q:
            node, color, distance = q.popleft()
        
            for nxt in color_map[1 - color][node]:
                if path[1 - color][nxt] == float("inf"):
                    path[1 - color][nxt] = distance + 1
                    q.append((nxt, 1 - color, distance + 1))
        
        for i in range(n):
            ans[i] = min(path[0][i], path[1][i])
            if ans[i] == float("inf"):
                ans[i] = -1
        return ans

test = Solution()
print(test.shortestAlternatingPaths(n = 5, redEdges = [[0,1],[1,2],[2,3],[3,4]], blueEdges = [[1,2],[2,3],[3,1]]))


