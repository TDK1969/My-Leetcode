"""
日期: 2024-06-30
题目: 目标和
链接: https://leetcode.cn/problems/target-sum/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # sum - target / 2 = neg
        s = sum(nums)
        if s - target < 0 or (s - target) & 1:
            return 0

        k = (s - target) // 2
        # 在nums中选若干个数，和为k的方案数
        # dp[i][j]表示前i个数中和为j的方案数
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i - 1] <= j:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
        
        return dp[-1][-1]

            
print(Solution().findTargetSumWays([1,1,1,1,1],3))      



"""
--TESTCASE BEGIN--
TestCase 0: [1,1,1,1,1],3
TestCase 1: [1],1
--TESTCASE END--
""" 
