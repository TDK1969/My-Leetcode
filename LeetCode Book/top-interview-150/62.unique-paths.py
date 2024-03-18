"""
日期: 2022-07-14
题目: 不同路径
链接: https://leetcode-cn.com/problems/unique-paths/
"""

from typing import *
from collections import *
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 状态转移方程 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        dp = [1 for _ in range(n)]
        for _ in range(m - 1):
            dp_nxt = [0 for _ in range(n)]
            dp_nxt[0] = 1
            for i in range(1, n):
                dp_nxt[i] = dp_nxt[i - 1] + dp[i]
            dp = dp_nxt
        return dp[-1]
        
    def uniquePaths(self, m: int, n: int) -> int:
        # 状态转移方程 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        dp = [1 for _ in range(n)]
        for _ in range(m - 1):
            for i in range(1, n):
                dp[i] += dp[i - 1]
        return dp[-1]
    
    def uniquePaths(self, m: int, n: int) -> int:
        k = min(m - 1, n - 1)
        ans = 1
        for i in range(k):
            ans = ans * (m + n - 2 - i) // (i + 1)
        return ans

test = Solution()
print(test.uniquePaths(m = 3, n = 7))