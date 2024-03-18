"""
日期: 2024-03-10
题目: Pow(x, n)
链接: https://leetcode-cn.com/problems/powx-n/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        flag = n >= 0
        n = abs(n)
        while n:
            if n & 1 == 1:
                ans *= x
            n >>= 1
            x *= x
        
        return ans if flag else 1 / ans

print(Solution().myPow(2.00000,10))
"""
--TESTCASE BEGIN--
TestCase 0: 2.00000,10
TestCase 1: 2.10000,3
TestCase 2: 2.00000,-2
--TESTCASE END--
""" 
