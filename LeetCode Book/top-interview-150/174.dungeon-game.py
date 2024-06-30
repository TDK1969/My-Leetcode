"""
日期: 2024-04-08
题目: 地下城游戏
链接: https://leetcode-cn.com/problems/dungeon-game/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        lowerest_k = -float("inf")
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = dungeon[0][0]
        if dungeon[0][0] <= 0:
            lowerest_k = dungeon[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + dungeon[i][0]
            if dp[i][0] <= 0:
                lowerest_k = max(lowerest_k, dp[i][0])
        
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + dungeon[0][i]
            if dp[0][i] <= 0:
                lowerest_k = max(lowerest_k, dp[0][i])
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + dungeon[i][j]
                if dp[i][j] <= 0:
                    lowerest_k = max(lowerest_k, dp[i][j])
        
        

"""
--TESTCASE BEGIN--
TestCase 0: [[-2,-3,3],[-5,-10,1],[10,30,-5]]
TestCase 1: [[0]]
--TESTCASE END--
""" 
