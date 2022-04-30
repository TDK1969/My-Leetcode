"""
题目: 统计网格图中没有被保卫的格子数
链接: https://leetcode-cn.com/problems/count-unguarded-cells-in-the-grid/
"""
from typing import *
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grids = [[0 for _ in range(n)] for _ in range(m)]
        for x, y in guards:
            grids[x][y] = 2
        for x, y in walls:
            grids[x][y] = 2
        
        for x_guard, y_guard in guards:
            for x in range(x_guard + 1, m):
                if grids[x][y_guard] == 0:
                    grids[x][y_guard] = 1
                elif grids[x][y_guard] == 2:
                    break

            for x in range(x_guard - 1, -1, -1):
                if grids[x][y_guard] == 0:
                    grids[x][y_guard] = 1
                elif grids[x][y_guard] == 2:
                    break
            
            for y in range(y_guard + 1, n):
                if grids[x_guard][y] == 0:
                    grids[x_guard][y] = 1
                elif grids[x_guard][y] == 2:
                    break
            
            for y in range(y_guard - 1, -1, -1):
                if grids[x_guard][y] == 0:
                    grids[x_guard][y] = 1
                elif grids[x_guard][y] == 2:
                    break
        ans = 0
        for x in range(m):
            for y in range(n):
                if grids[x][y] == 0:
                    ans += 1
        return ans
            

            