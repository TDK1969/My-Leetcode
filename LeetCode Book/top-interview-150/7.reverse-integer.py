"""
日期: 2022-07-14
题目: 整数反转
链接: https://leetcode-cn.com/problems/reverse-integer/
"""

from typing import *
from collections import *
class Solution:
    def reverse(self, x: int) -> int:
        flag = x < 0
        if x == 0:
            return 0
        boundary = (1 << 31) - (0 if flag else 1)
        
        t = abs(x)

        ans = 0
        while t:
            if boundary - ans * 10 >= t % 10:
                ans = ans * 10 + t % 10
                t = t // 10
            else:
                return 0
        return -ans if flag else ans




test = Solution()
print(test.reverse(123))