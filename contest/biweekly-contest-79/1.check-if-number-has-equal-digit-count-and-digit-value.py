"""
题目: 判断一个数的数字计数是否等于数位的值
链接: https://leetcode-cn.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
"""

from typing import *
from collections import *

class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for index, value in enumerate(num):
            if c[str(index)] != int(value):
                return False
        return True