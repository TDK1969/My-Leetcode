"""
日期: 2023-02-20
题目: 最好的扑克手牌
链接: https://leetcode-cn.com/problems/best-poker-hand/
"""

from typing import *
from collections import *
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        c = Counter(ranks)
        s = set(suits)
        if len(s) == 1:
            return "Flush"
        
        if max(c.values()) >= 3:
            return "Three of a Kind"
        
        if max(c.values()) == 2:
            return "Pair"
        
        if len(c) == 5:
            return "High Card"