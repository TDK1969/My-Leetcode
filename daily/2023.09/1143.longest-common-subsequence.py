"""
日期: 2023-09-18
题目: 最长公共子序列
链接: https://leetcode-cn.com/problems/longest-common-subsequence/
"""

from typing import *
from collections import *
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        #dp = [[0 for _ in range(n2 + 1)] for _  in range(n1 + 1)]
        # 进行空间优化,因为只需要用到dp[i - 1][j]
        dp1 = [0 for _ in range(n2 + 1)]
        dp2 = [0 for _ in range(n2 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp2[j] = dp1[j - 1] + 1
                else:
                    dp2[j] = max(dp2[j - 1], dp1[j])
            dp1 = dp2
            dp2 = [0 for _ in range(n2 + 1)]
        return dp1[-1]

test = Solution()
print(test.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))