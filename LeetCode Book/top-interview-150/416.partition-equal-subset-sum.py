"""
日期: 2023-11-09
题目: 分割等和子集
链接: https://leetcode-cn.com/problems/partition-equal-subset-sum/
"""

from typing import *
from collections import *
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        nums_sum = sum(nums)
        if nums_sum & 1:
            return False
        target = nums_sum >> 1

        nums_max = max(nums)
        if nums_max > target:
            return False
        
        # dp[i][j]表示在nums下标[0, i]是否能够选取若干元素,使其元素和为j
        # 边界:
        # 1. dp[i][0] = True,因为不选取元素就可以使元素和为0
        # 2. dp[0][nums[0]] = True,选下标为0可以使元素和为nums[0]
        dp = [True] + [False for _ in range(target)]
        dp[nums[0]] = True

        for i in range(1, n):
            for j in range(target, -1, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j - nums[i]]

        return dp[-1]

print(Solution().canPartition([1,5,11,5]))
        