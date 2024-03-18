"""
日期: 2024-02-08
题目: 寻找旋转排序数组中的最小值
链接: https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[l] < nums[mid] < nums[r]:
                return nums[l]
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[r]

print(Solution().findMin([4,5,6,7,0,1,2]))

"""
--TESTCASE BEGIN--
TestCase 0: [3,4,5,1,2]
TestCase 1: [4,5,6,7,0,1,2]
TestCase 2: [11,13,15,17]
--TESTCASE END--
""" 
