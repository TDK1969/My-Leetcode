"""
题目: 价格减免
链接: https://leetcode-cn.com/problems/apply-discount-to-prices/
"""

from typing import *
from collections import *
import re
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        def count(matched):
            value = matched.group()
            value = float(value[1:])
            value = round(value * (1 - discount / 100), 2) 
            return "$%.2f "%(value)
        res = re.sub("\$\d+(\.\d+)? ", count, sentence)
        return res

test = Solution()
print(test.discountPrices(sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50))
