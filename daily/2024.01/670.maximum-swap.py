"""
日期: 2024-01-22
题目: 最大交换
链接: https://leetcode.cn/problems/maximum-swap/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maximumSwap(self, num: int) -> int:
        digit = []
        t = num
        while t:
            digit.append(t % 10)
            t = t // 10
        digit.reverse()
        n = len(digit)
        max_num = sorted(digit, reverse=True)
        if digit == max_num:
            return num
        for i in range(n):
            if digit[i] != max_num[i]:
                # 需要将digit[i]与max_num[i]交换
                for j in range(n - 1, -1, -1):
                    if digit[j] == max_num[i]:
                        digit[i], digit[j] = max_num[i], digit[i]
                        return int("".join([str(i) for i in digit]))


print(Solution().maximumSwap(9973))

"""
--TESTCASE BEGIN--
TestCase 0: 2736
TestCase 1: 9973
--TESTCASE END--
""" 
