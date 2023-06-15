"""
题目: 统计桌面上的不同数字
链接: https://leetcode-cn.com/problems/count-distinct-numbers-on-board/
"""

from typing import *
from collections import *
class Solution:
    def distinctIntegers(self, n: int) -> int:
        return n - 1 if n != 1 else 1