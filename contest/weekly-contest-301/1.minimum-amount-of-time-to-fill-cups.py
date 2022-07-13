"""
题目: 装满杯子需要的最短总时长
链接: https://leetcode-cn.com/problems/minimum-amount-of-time-to-fill-cups/
"""

from typing import *
from collections import *
import heapq
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        h = []
        
        for num in amount:
            if num:
                h.append(num)
        
        ans = 0
        
            
