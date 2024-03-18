"""
日期: 2024-01-22
题目: 搜索旋转排序数组
链接: https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid] <= nums[r]:
                # [l, r]为有序
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

print(Solution().search([4,5,6,7,0,1,2],0))

"""
--TESTCASE BEGIN--
TestCase 0: [4,5,6,7,0,1,2],0
TestCase 1: [4,5,6,7,0,1,2],3
TestCase 2: [1],0
--TESTCASE END--
""" 
