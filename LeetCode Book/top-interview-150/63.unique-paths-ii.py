"""
日期: 2024-03-20
题目: 不同路径 II
链接: https://leetcode-cn.com/problems/unique-paths-ii/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1 - obstacleGrid[0][0]]
        for num in obstacleGrid[0][1:]:
            if dp[-1] == 0:
                dp.append(0)
            else:
                dp.append(1 - num)
        
        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]

        return dp[-1]

print(Solution().uniquePathsWithObstacles([[0], [1]]))
"""
--TESTCASE BEGIN--
TestCase 0: [[0,0,0],[0,1,0],[0,0,0]]
TestCase 1: [[0,1],[0,0]]
--TESTCASE END--
""" 
