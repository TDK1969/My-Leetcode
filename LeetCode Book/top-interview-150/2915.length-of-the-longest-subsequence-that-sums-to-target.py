"""
日期: 2024-03-29
题目: 和为目标值的最长子序列的长度
链接: https://leetcode-cn.com/problems/length-of-the-longest-subsequence-that-sums-to-target/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums = [num for num in nums if num <= target]
        n = len(nums)
        if n == 0:
            return -1
        # dp[i][j] 表示前i个数中和为j的子序列的最大长度
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
        presum = []
        for i in range(n):
            if i == 0:
                presum.append(nums[i])
            else:
                presum.append(nums[i] + presum[-1])
            dp[i][0] = 0
        dp[0][nums[0]] = 1
        for i in range(1, n):
            for j in range(1, min(target, presum[i]) + 1):
                dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - nums[i]] + 1) if nums[i] <= j and dp[i - 1][j - nums[i]] != -1 else -1)

        return dp[-1][-1] if dp[-1][-1] != 0 else -1
    def lengthOfLongestSubsequence1(self, nums: List[int], target: int) -> int:
        nums = [num for num in nums if num <= target]
        n = len(nums)

        dp = [-float("inf")] * (target + 1)
        dp[0] = 0
        s = 0
        for num in nums:
            s = min(s + num, target)
            for i in range(s, num - 1, -1):
                dp[i] = max(dp[i], dp[i - num] + 1)
        return dp[-1] if dp[-1] > 0 else -1



print(Solution().lengthOfLongestSubsequence([1,2,3,4,5],9))


"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,4,5],9
TestCase 1: [4,1,3,2,1,5],7
TestCase 2: [1,1,5,4,5],3
--TESTCASE END--
""" 
