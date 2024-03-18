"""
日期: 2024-03-07
题目: 爬楼梯
链接: https://leetcode-cn.com/problems/climbing-stairs/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def climbStairs(self, n: int) -> int:
        c1 = c2 = 1
        for _ in range(1, n):
            c1, c2 = c2, c1 + c2
        return c2

"""
--TESTCASE BEGIN--
TestCase 0: 2
TestCase 1: 3
--TESTCASE END--
""" 
