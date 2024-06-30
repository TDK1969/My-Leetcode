"""
日期: 2024-06-12
题目: 取整购买后的账户余额
链接: https://leetcode.cn/problems/account-balance-after-rounded-purchase/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - int(purchaseAmount / 10 + 0.5) * 10

"""
--TESTCASE BEGIN--
TestCase 0: 9
TestCase 1: 15
--TESTCASE END--
""" 
