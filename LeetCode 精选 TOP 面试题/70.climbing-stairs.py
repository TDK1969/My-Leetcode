"""
日期: 2022-07-14
题目: 爬楼梯
链接: https://leetcode-cn.com/problems/climbing-stairs/
"""

from typing import *
from collections import *
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 3)]
        dp[0] = 1
        for i in range(0, n):
            dp[i + 1] += dp[i]
            dp[i + 2] += dp[i]
        return dp[-3]

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b



test = Solution()
print(test.climbStairs(5))