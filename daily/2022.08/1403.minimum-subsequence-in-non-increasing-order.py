"""
日期: 2022-08-04
题目: 非递增顺序的最小子序列
链接: https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order/
"""

from typing import *
from collections import *
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        s = sum(nums)
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            if t * 2 > s:
                return nums[:i + 1]

