"""
日期: 2022-06-03
题目: 连续整数求和
链接: https://leetcode-cn.com/problems/consecutive-numbers-sum/
"""

from typing import *
from collections import *
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        cnt = 0

        for k in range(1, n + 1):
            if k * (1 + k) > 2 * n:
                break
            if k & 1 and n % k == 0:
                cnt += 1
            elif k & 1 == 0 and n % k != 0 and (2 * n) % k == 0:
                cnt += 1
        return cnt
