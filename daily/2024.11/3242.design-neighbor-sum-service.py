"""
日期: 2024-11-09
题目: 设计相邻元素求和服务
链接: https://leetcode.cn/problems/design-neighbor-sum-service/
"""

from typing import *
from collections import *
from leetcode_utils import *
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.index = dict()
        self.n = len(self.grid)
        for i in range(self.n):
            for j in range(self.n):
                self.index[self.grid[i][j]] = (i, j)
        

    def adjacentSum(self, value: int) -> int:
        x, y = self.index[value]
        ans = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                ans += self.grid[nx][ny]
        return ans

    def diagonalSum(self, value: int) -> int:
        x, y = self.index[value]
        ans = 0
        directions = [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                ans += self.grid[nx][ny]
        return ans


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)

"""
--TESTCASE BEGIN--
TestCase 0: ["NeighborSum","adjacentSum","adjacentSum","diagonalSum","diagonalSum"],[[[[0,1,2],[3,4,5],[6,7,8]]],[1],[4],[4],[8]]
TestCase 1: ["NeighborSum","adjacentSum","diagonalSum"],[[[[1,2,0,3],[4,7,15,6],[8,9,10,11],[12,13,14,5]]],[15],[9]]
--TESTCASE END--
""" 
