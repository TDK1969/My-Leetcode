"""
日期: 2023-10-26
题目: 轮转数组
链接: https://leetcode-cn.com/problems/rotate-array/
"""

from typing import *
from collections import *
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums.reverse()
        
        def reverse(left: int, right: int):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, k - 1)
        reverse(k, n - 1)

print(Solution().rotate([1,2,3,4,5], 2))