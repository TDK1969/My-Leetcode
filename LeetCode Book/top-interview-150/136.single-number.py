"""
日期: 2024-01-19
题目: 只出现一次的数字
链接: https://leetcode-cn.com/problems/single-number/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = 0
        for num in nums:
            k ^= num
        return k

"""
--TESTCASE BEGIN--
TestCase 0: [2,2,1]
TestCase 1: [4,1,2,1,2]
TestCase 2: [1]
--TESTCASE END--
""" 
