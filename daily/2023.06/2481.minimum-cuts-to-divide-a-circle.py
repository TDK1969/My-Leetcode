"""
日期: 2023-06-17
题目: 分割圆的最少切割次数
链接: https://leetcode-cn.com/problems/minimum-cuts-to-divide-a-circle/
"""

from typing import *
from collections import *
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if 180 % n == 0 and n & 1 == 0:
            return n // 2
        else:
            return n
