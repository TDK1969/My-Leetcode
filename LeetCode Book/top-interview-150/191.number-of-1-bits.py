"""
日期: 2024-01-19
题目: 位1的个数
链接: https://leetcode-cn.com/problems/number-of-1-bits/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n & 1
            n >>= 1
        return cnt
        

"""
--TESTCASE BEGIN--
TestCase 0: 00000000000000000000000000001011
TestCase 1: 00000000000000000000000010000000
TestCase 2: 11111111111111111111111111111101
--TESTCASE END--
""" 
