"""
日期: 2024-07-03
题目: 哈沙德数
链接: https://leetcode.cn/problems/harshad-number/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        t = x
        while t:
            s += t % 10
            t = t // 10
        if x % s == 0:
            return s
        else:
            return -1

"""
--TESTCASE BEGIN--
TestCase 0: 18
TestCase 1: 23
--TESTCASE END--
""" 
