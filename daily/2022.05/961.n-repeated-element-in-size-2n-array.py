"""
日期: 2022-05-21
题目: 在长度 2N 的数组中找出重复 N 次的元素
链接: https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array/
"""

from typing import *
from collections import *
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        if nums[0] == nums[2]:
            return nums[0]
        if nums[0] == nums[-1]:
            return nums[0]
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        
        return nums[1]