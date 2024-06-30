"""
日期: 2024-03-20
题目: 编辑距离
链接: https://leetcode-cn.com/problems/edit-distance/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        # dp[i][j]: word1的前i个字符转成word2的前j个字符的编辑距离
        dp = [[float("inf") for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):
            dp[i + 1][0] = i + 1
        for j in range(m):
            dp[0][j + 1] = j + 1
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        
        return dp[-1][-1]

print(Solution().minDistance("horse","ros"))

"""
--TESTCASE BEGIN--
TestCase 0: "horse","ros"
TestCase 1: "intention","execution"
--TESTCASE END--
""" 
