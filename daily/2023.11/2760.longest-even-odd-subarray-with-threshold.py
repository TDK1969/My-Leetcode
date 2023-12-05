"""
日期: 2023-11-16
题目: 最长奇偶子数组
链接: https://leetcode-cn.com/problems/longest-even-odd-subarray-with-threshold/
"""

from typing import *
from collections import *
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        l = 0
        ans = 0

        while l < n:
            if nums[l] & 1 == 0 and nums[l] <= threshold:
                r = l + 1
                while r < n and nums[r] <= threshold and nums[r] & 1 == (r - l) & 1:
                    r += 1
                ans = max(ans, r - l)
                l = r
            else:
                l += 1
        
        return ans

print(Solution().longestAlternatingSubarray(nums = [2,5,2,5,8,5], threshold = 6))