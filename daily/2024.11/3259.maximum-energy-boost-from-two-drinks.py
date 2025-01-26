"""
日期: 2024-11-01
题目: 超级饮料的最大强化能量
链接: https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)

        dp = [[0, 0] for _ in range(n + 1)]
        dp[1][0] = energyDrinkA[0]
        dp[1][1] = energyDrinkB[0]

        for i in range(2, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 2][1]) + energyDrinkA[i - 1]
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0]) + energyDrinkB[i - 1]

        return max(dp[-1])
print(Solution().maxEnergyBoost([4,1,1],[1,1,3]))   

"""
--TESTCASE BEGIN--
TestCase 0: [1,3,1],[3,1,1]
TestCase 1: [4,1,1],[1,1,3]
--TESTCASE END--
""" 
