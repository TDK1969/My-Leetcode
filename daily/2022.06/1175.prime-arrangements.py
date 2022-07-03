"""
日期: 2022-06-30
题目: 质数排列
链接: https://leetcode-cn.com/problems/prime-arrangements/
"""

from typing import *
from collections import *
import bisect
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        m = bisect.bisect_right(primes, n)
        def factorial(n: int) -> int:
            res = 1
            for i in range(1, n + 1):
                res = (res * i) % (10 ** 9 + 7)
            return res
        return (factorial(m) * factorial(n - m)) % (10 ** 9 + 7)
        # m! * (n - m)!

test = Solution()
print(test.numPrimeArrangements(100))