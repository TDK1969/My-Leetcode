"""
日期: 2022-09-01
题目: 商品折扣后的最终价格
链接: https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop/
"""

from typing import *
from collections import *
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = prices[:]
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    ans[i] -= prices[j]
                    break
        return ans