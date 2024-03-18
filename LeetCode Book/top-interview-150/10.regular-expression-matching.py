"""
日期: 2022-07-14
题目: 正则表达式匹配
链接: https://leetcode-cn.com/problems/regular-expression-matching/
"""

from typing import *
from collections import *
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True

        def match(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] |= dp[i][j - 2]
                    if match(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if match(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
        return dp[-1][-1]

test = Solution()
print(test.isMatch(s = "aa", p = "a*"))