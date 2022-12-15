"""
日期: 2022-10-21
题目: 股票价格跨度
链接: https://leetcode-cn.com/problems/online-stock-span/
"""

from typing import *
from collections import *
class StockSpanner:

    def __init__(self):
        self.stack = []


    def next(self, price: int) -> int:
        cnt = 1
        while self.stack and self.stack[-1][0] <= price:
            cnt += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, cnt))
        return cnt
