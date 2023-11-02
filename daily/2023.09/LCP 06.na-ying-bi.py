"""
日期: 2023-09-20
题目: 拿硬币
链接: https://leetcode-cn.com/problems/na-ying-bi/
"""

from typing import *
from collections import *
class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum((coin + 1) // 2 for coin in coins)