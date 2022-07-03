"""
日期: 2022-07-03
题目: 下一个更大元素 III
链接: https://leetcode-cn.com/problems/next-greater-element-iii/
"""

from typing import *
from collections import *
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        if sorted(digits)[::-1] == digits:
            return -1
        n = len(digits)

        for i in range(n - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                for j in range(n - 1, i, -1):
                    if digits[j] > digits[i]:
                        digits[j], digits[i] = digits[i], digits[j]
                        digits[i + 1:] = sorted(digits[i + 1:])
                        break
                break
        
        res = int("".join([str(i) for i in digits]))
        return res if res < 2 ** 32 else -1

test = Solution()
print(test.nextGreaterElement(230241))