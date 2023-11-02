"""
日期: 2023-10-16
题目: 只出现一次的数字 III
链接: https://leetcode-cn.com/problems/single-number-iii/
"""

from typing import *
from collections import *
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = 0
        for num in nums:
            c ^= num
        l = c & -c

        type1 = type2 = 0
        for num in nums:
            if num & l:
                type1 ^= num
            else:
                type2 ^= num
        
        return [type1, type2]