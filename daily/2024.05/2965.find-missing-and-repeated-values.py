"""
日期: 2024-05-31
题目: 找出缺失和重复的数字
链接: https://leetcode.cn/problems/find-missing-and-repeated-values/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        k = 0
        ans = [-1, -1]
        while k < n ** 2:
            i, j = k // n, k % n
            while grid[i][j] != k + 1 and grid[(grid[i][j] - 1) // n][(grid[i][j] - 1) % n] != grid[i][j]:
                x, y = grid[i][j], grid[(grid[i][j] - 1) // n][(grid[i][j] - 1) % n]
                grid[i][j] = y
                grid[(x - 1) // n][(x - 1) % n] = x
            if grid[i][j] != k + 1:
                ans[0], ans[1] = grid[i][j], k + 1
                break
            k += 1
        return ans
print(Solution().findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))

"""
--TESTCASE BEGIN--
TestCase 0: [[1,3],[2,2]]
TestCase 1: [[9,1,7],[8,9,2],[3,4,6]]
--TESTCASE END--
""" 
