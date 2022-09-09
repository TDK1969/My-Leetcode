"""
日期: 2022-07-14
题目: Pow(x, n)
链接: https://leetcode-cn.com/problems/powx-n/
"""

from typing import *
from collections import *
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        if n == 0:
            return 1.0
        flag = n < 0
        n = abs(n)
        while n:
            if n & 1:
                ans *= x
            n >>= 1
            x = x * x
        return ans if not flag else 1 / ans

test = Solution()
print(test.myPow(2.0, -2))