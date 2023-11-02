"""
日期: 2023-09-15
题目: 宝石补给
链接: https://leetcode-cn.com/problems/WHnhjV/
"""

from typing import *
from collections import *
class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for x, y in operations:
            t = gem[x] // 2
            gem[x] -= t
            gem[y] += t
        return max(gem) - min(gem)