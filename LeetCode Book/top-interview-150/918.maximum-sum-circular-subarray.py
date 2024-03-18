"""
日期: 2024-01-20
题目: 环形子数组的最大和
链接: https://leetcode-cn.com/problems/maximum-sum-circular-subarray/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        pre_max, max_res = nums[0], nums[0]
        pre_min, min_res = nums[0], nums[0]
        for num in nums[1:]:
            pre_max = max(pre_max + num, num)
            max_res = max(max_res, pre_max)
            pre_min = min(pre_min + num, num)
            min_res = min(min_res, pre_min)
        if max_res < 0:
            return max_res
        else:
            return max(max_res, sum(nums) - min_res)



"""
--TESTCASE BEGIN--
TestCase 0: [1,-2,3,-2]
TestCase 1: [5,-3,5]
TestCase 2: [-3,-2,-3]
--TESTCASE END--
""" 
