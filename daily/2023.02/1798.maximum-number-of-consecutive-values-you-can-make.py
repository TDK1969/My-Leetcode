"""
日期: 2023-02-04
题目: 你能构造出连续值的最大数目
链接: https://leetcode-cn.com/problems/maximum-number-of-consecutive-values-you-can-make/
"""

from typing import *
from collections import *
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ans = 0
        for coin in coins:
            if coin <= ans:
                ans += coin
            else:
                break
        return ans