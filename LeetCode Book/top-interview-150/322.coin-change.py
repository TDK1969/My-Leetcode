"""
日期: 2024-03-07
题目: 零钱兑换
链接: https://leetcode-cn.com/problems/coin-change/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        validCoins = [coin for coin in coins if coin <= amount]
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in validCoins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] != float("inf") else -1

print(Solution().coinChange([2],3))


"""
--TESTCASE BEGIN--
TestCase 0: [1,2,5],11
TestCase 1: [2],3
TestCase 2: [1],0
--TESTCASE END--
""" 
