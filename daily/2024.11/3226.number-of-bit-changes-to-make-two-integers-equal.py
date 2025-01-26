"""
日期: 2024-11-02
题目: 使两个整数相等的位更改次数
链接: https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        while n:
            if n & 1 == 0 and k & 1 == 1:
                return -1
            elif n & 1 == 1 and k & 1 == 0:
                ans += 1
            n = n >> 1
            k = k >> 1
        if k:
            return -1
        else:
            return ans
        
        
        

"""
--TESTCASE BEGIN--
TestCase 0: 13,4
TestCase 1: 21,21
TestCase 2: 14,13
--TESTCASE END--
""" 
