"""
日期: 2024-03-09
题目: 回文数
链接: https://leetcode-cn.com/problems/palindrome-number/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        p, q = x, 0
        while p:
            q = q * 10 + p % 10
            p = p // 10
        return q == x

"""
--TESTCASE BEGIN--
TestCase 0: 121
TestCase 1: -121
TestCase 2: 10
--TESTCASE END--
""" 
