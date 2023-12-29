"""
日期: 2023-12-24
题目: 岛屿数量
链接: https://leetcode-cn.com/problems/number-of-islands/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans = 0

        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    q = deque()
                    q.append((i, j))

                    while q:
                        x, y = q.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" and (nx, ny) not in visited:
                                visited.add((nx, ny))
                                q.append((nx, ny))
                    
                    ans += 1
        return ans


"""
--TESTCASE BEGIN--
TestCase 0: [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
TestCase 1: [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
--TESTCASE END--
""" 
print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))