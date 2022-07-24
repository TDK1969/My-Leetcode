"""
日期: 2022-07-14
题目: 两数之和
链接: https://leetcode-cn.com/problems/two-sum/
"""

from typing import *
from collections import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, num in enumerate(nums):
            index[num] = i
        
        for i, num in enumerate(nums):
            if target - num in index:
                return [i, index[target - num]]
            