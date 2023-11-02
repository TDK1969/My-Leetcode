"""
日期: 2023-10-20
题目: 整数转罗马数字
链接: https://leetcode-cn.com/problems/integer-to-roman/
"""

from typing import *
from collections import *
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        a, b, c, d = num // 1000, (num // 100) % 10, (num // 10) % 10, num % 10
        # 处理千位
        ans += "M" * a

        # 处理百位
        