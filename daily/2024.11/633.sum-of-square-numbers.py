"""
日期: 2024-11-04
题目: 平方数之和
链接: https://leetcode.cn/problems/sum-of-square-numbers/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        for i in range(2 ** 16):
            if i ** 2 > c:
                break
            squares.add(i ** 2)
        
        for square in squares:
            if c - square in squares:
                return True
        return False

        

"""
--TESTCASE BEGIN--
TestCase 0: 5
TestCase 1: 3
--TESTCASE END--
""" 
