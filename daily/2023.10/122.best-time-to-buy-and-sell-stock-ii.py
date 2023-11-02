"""
日期: 2023-10-02
题目: 买卖股票的最佳时机 II
链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

from typing import *
from collections import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices))])
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                ans += prices[i] - prices[i - 1]
        return ans

