"""
日期: 2023-02-11
题目: 装满杯子需要的最短总时长
链接: https://leetcode-cn.com/problems/minimum-amount-of-time-to-fill-cups/
"""

from typing import *
from collections import *
class Solution:
    def fillCups(self, amount: List[int]) -> int: 
        amount.sort(reverse=True)
        