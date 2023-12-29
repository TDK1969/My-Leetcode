"""
日期: 2023-12-18
题目: 寻找峰值
链接: https://leetcode-cn.com/problems/find-peak-element/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # 一直往高的地方找一定能找到,因为边界是负无穷
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
            



"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,1]
TestCase 1: [1,2,1,3,5,6,4]
--TESTCASE END--
""" 
print(Solution().findPeakElement([1,2,1,3,5,6,4]))