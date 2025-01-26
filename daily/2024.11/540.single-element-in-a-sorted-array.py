"""
日期: 2024-11-10
题目: 有序数组中的单一元素
链接: https://leetcode.cn/problems/single-element-in-a-sorted-array/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            half = (right - left) // 2
            if half & 1:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    right = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    right = mid
                elif nums[mid] == nums[mid + 1]:
                    left = mid

        return nums[right]
    
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))


        

"""
--TESTCASE BEGIN--
TestCase 0: [1,1,2,3,3,4,4,8,8]
TestCase 1: [3,3,7,7,10,11,11]
--TESTCASE END--
""" 
