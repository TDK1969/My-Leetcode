"""
题目: 反转之后的数字和
链接: https://leetcode-cn.com/problems/sum-of-number-and-its-reverse/
"""

from typing import *
from collections import *
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(0, num + 1):
            if i + int(str(i)[::-1]) == num:
                return True
        return False
