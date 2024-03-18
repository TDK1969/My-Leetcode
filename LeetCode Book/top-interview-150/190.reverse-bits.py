"""
日期: 2024-01-19
题目: 颠倒二进制位
链接: https://leetcode-cn.com/problems/reverse-bits/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        k = n
        for _ in range(32):
            ans = (ans << 1) + (k & 1)
            k >>= 1
        return ans

print(Solution().reverseBits(0b00000010100101000001111010011100))

"""
--TESTCASE BEGIN--
TestCase 0: 00000010100101000001111010011100
TestCase 1: 11111111111111111111111111111101
--TESTCASE END--
""" 
