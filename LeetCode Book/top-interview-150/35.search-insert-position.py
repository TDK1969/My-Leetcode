"""
日期: 2024-01-21
题目: 搜索插入位置
链接: https://leetcode-cn.com/problems/search-insert-position/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return r

print(Solution().searchInsert([1,3,5,5,5,5,5,5,5,6],5))


"""
--TESTCASE BEGIN--
TestCase 0: [1,3,5,6],5
TestCase 1: [1,3,5,6],2
TestCase 2: [1,3,5,6],7
--TESTCASE END--
""" 
