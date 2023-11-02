"""
日期: 2023-10-01
题目: 买卖股票的最佳时机
链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import *
from collections import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        pre = prices[0]
        for i in prices:
            if i < pre:
                pre = i
            else:
                ans = max(ans, i - pre)
        return ans