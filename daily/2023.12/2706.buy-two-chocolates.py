"""
日期: 2023-12-29
题目: 购买两块巧克力
链接: https://leetcode-cn.com/problems/buy-two-chocolates/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        low1 = 101
        low2 = 102
        for price in prices:
            if price <= low1:
                low1, low2 = price, low1
            elif price < low2:
                low2 = price
        
        if low1 + low2 > money:
            return money
        else:
            return money - low1 - low2



"""
--TESTCASE BEGIN--
TestCase 0: [1,2,2],3
TestCase 1: [3,2,3],3
--TESTCASE END--
""" 

print(Solution().buyChoco([3,2,3],3))
