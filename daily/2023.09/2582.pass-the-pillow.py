"""
日期: 2023-09-26
题目: 递枕头
链接: https://leetcode-cn.com/problems/pass-the-pillow/
"""

from typing import *
from collections import *
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        return 1 + min(time % (2 * (n - 1)), 2 * (n - 1) - time % (2 * (n - 1)))