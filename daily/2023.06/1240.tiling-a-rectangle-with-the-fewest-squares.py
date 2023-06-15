"""
日期: 2023-06-08
题目: 铺瓷砖
链接: https://leetcode-cn.com/problems/tiling-a-rectangle-with-the-fewest-squares/
"""

from typing import *
from collections import *
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = i + 1
        for i in range(m):
            dp[0][i] = i + 1
        for i in range(min(n, m)):
            dp[i][i] = 1
        