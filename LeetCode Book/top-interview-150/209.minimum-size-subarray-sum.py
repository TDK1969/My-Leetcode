"""
日期: 2023-10-24
题目: 长度最小的子数组
链接: https://leetcode-cn.com/problems/minimum-size-subarray-sum/
"""

from typing import *
from collections import *
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        left = right = s = 0
        while right <= len(nums):
            while left < right and s >= target:
                s -= nums[left]
                ans = min(ans, right - left)
                left += 1
            if right == len(nums):
                break
            s += nums[right]
            right += 1
            
        return 0 if ans == float("inf") else ans

test = Solution()
print(test.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))


