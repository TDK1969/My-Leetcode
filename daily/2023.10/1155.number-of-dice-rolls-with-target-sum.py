"""
日期: 2023-10-24
题目: 掷骰子等于目标和的方法数
链接: https://leetcode-cn.com/problems/number-of-dice-rolls-with-target-sum/
"""

from typing import *
from collections import *
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        if target < n or target > n * k:
            return 0
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for j in range(1, target + 1):
            for i in range(1, n + 1):
                for x in range(1, k + 1):
                    dp[i][j] = dp[i - 1][j - x]
        # dp[i][j] = sum(dp[i - 1][j - x]) for x in range(1, k)

        return dp[-1][-1]
    
test = Solution()
print(test.numRollsToTarget(n = 30, k = 30, target = 500))
