"""
日期: 2023-02-10
题目: 掷骰子模拟
链接: https://leetcode-cn.com/problems/dice-roll-simulation/
"""

from typing import *
from collections import *
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(6)]
        dp[0][1] = dp[1][1] = dp[2][1] = dp[3][1] = dp[4][1] = dp[5][1] = 1
        mod = 10 ** 9 + 7

        # dp[i][j]表示长度为i,以j结尾的骰子序列
        for i in range(2, n + 1):
            for j in range(6):
                for k in range(max(0, i - rollMax[j]), i):
                    if k == 0:
                        dp[j][i] = (dp[j][i] + 1) % mod
                    else:
                        dp[j][i] = (dp[j][i] + sum(dp[p][k] for p in range(6) if p != j) ) % mod
        
        return (dp[0][-1] + dp[1][-1] + dp[2][-1] + dp[3][-1] + dp[4][-1] + dp[5][-1]) % mod

test = Solution()
print(test.dieSimulator(n = 3, rollMax = [1,1,1,2,2,3]))

