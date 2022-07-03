"""
日期: 2022-06-25
题目: 粉刷房子
链接: https://leetcode-cn.com/problems/JEj789/
"""

from typing import *
from collections import *
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0, 0, 0] for _ in range(n)]
        for i in range(3):
            dp[0][i] = costs[0][i]
        
        for i in range(1, n):
            for j in range(3):
                dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + costs[i][j]
        
        return min(dp[-1])