"""
日期: 2022-11-12
题目: 多米诺和托米诺平铺
链接: https://leetcode-cn.com/problems/domino-and-tromino-tiling/
"""

from typing import *
from collections import *
class Solution:
    def numTilings(self, n: int) -> int:
        dp = 