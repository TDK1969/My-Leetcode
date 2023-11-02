"""
日期: 2023-10-17
题目: 倍数求和
链接: https://leetcode-cn.com/problems/sum-multiples/
"""

from typing import *
from collections import *

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def func(m: int):
            k = n // m
            return m * (1 + k) * k // 2
        return func(3) + func(5) + func(7) - func(3 * 5) - func(3 * 7) - func(5 * 7) + func(3 * 5 * 7)

test = Solution()
print(test.sumOfMultiples(10))
 