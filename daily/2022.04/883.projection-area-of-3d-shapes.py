"""
日期: 2022-04-26
题目: 三维形体投影面积
链接: https://leetcode-cn.com/problems/projection-area-of-3d-shapes/
"""
from typing import List
from collections import defaultdict

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)

        for x in range(n):
            y_max = 0
            for y in range(n):
                z = grid[x][y]
                if z > 0:
                    ans += 1
                if z > y_max:
                    y_max = z
            ans += y_max
    
        for y in range(n):
            x_max = 0
            for x in range(n):
                z = grid[x][y]  
                if z > x_max:
                    x_max = z
            ans += x_max
        
        return ans

test = Solution()
print(test.projectionArea([[1,2],[3,4]]))