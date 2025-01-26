"""
日期: 2025-01-22
题目: 你可以获得的最大硬币数目
链接: https://leetcode.cn/problems/maximum-number-of-coins-you-can-get/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        ans = 0
        for i in range(1, n * 2 // 3 + 1, 2):
            ans += piles[i]
        return ans 
        
print(Solution().maxCoins([2,4,5]))
"""
--TESTCASE BEGIN--
TestCase 0: [2,4,1,2,7,8]
TestCase 1: [2,4,5]
TestCase 2: [9,8,7,6,5,1,2,3,4]
--TESTCASE END--
""" 
