"""
日期: 2024-03-09
题目: x 的平方根 
链接: https://leetcode-cn.com/problems/sqrtx/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) >> 1
            if mid ** 2 <= x and (mid + 1) ** 2 > x:
                return mid
            elif mid ** 2 > x:
                r = mid - 1
            else:
                l = mid + 1
        return l
                
print(Solution().mySqrt(2**32))
"""
--TESTCASE BEGIN--
TestCase 0: 4
TestCase 1: 8
--TESTCASE END--
""" 
