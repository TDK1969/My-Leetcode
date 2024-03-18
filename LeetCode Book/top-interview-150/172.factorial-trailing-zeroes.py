"""
日期: 2024-03-09
题目: 阶乘后的零
链接: https://leetcode-cn.com/problems/factorial-trailing-zeroes/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            ans += n // 5
            n = n // 5
        return ans

print(Solution().trailingZeroes(30))

"""
--TESTCASE BEGIN--
TestCase 0: 3
TestCase 1: 5
TestCase 2: 0
--TESTCASE END--
""" 
