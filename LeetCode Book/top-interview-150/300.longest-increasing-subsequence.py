"""
日期: 2024-03-07
题目: 最长递增子序列
链接: https://leetcode-cn.com/problems/longest-increasing-subsequence/
"""

from typing import *
from collections import *
from leetcode_utils import *
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]表示以nums[i]为结尾的最长递增子序列的长度
        n = len(nums)
        dp = [0 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return max(dp)
    def lengthOfLIS2(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            i = bisect.bisect_left(dp, num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)
            

print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))

"""
--TESTCASE BEGIN--
TestCase 0: [10,9,2,5,3,7,101,18]
TestCase 1: [0,1,0,3,2,3]
TestCase 2: [7,7,7,7,7,7,7]
--TESTCASE END--
""" 
