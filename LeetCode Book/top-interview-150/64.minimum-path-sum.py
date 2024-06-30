"""
日期: 2024-03-20
题目: 最小路径和
链接: https://leetcode-cn.com/problems/minimum-path-sum/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = []
        for num in grid[0]:
            if len(dp) == 0:
                dp.append(num)
            else:
                dp.append(dp[-1] + num)
        for i in range(1, n):
            dp[0] += grid[i][0]
            for j in range(1, m):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        
        return dp[-1]

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))


"""
--TESTCASE BEGIN--
TestCase 0: [[1,3,1],[1,5,1],[4,2,1]]
TestCase 1: [[1,2,3],[4,5,6]]
--TESTCASE END--
""" 
