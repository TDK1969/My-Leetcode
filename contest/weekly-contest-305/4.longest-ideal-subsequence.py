"""
题目: 最长理想子序列
链接: https://leetcode-cn.com/problems/longest-ideal-subsequence/
"""

from typing import *
from collections import *
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0 for _ in range(26)]
        for i in s:
            a = ord(i) - ord("a")
            dp[a] = 1 + max(dp[max(a - k, 0):a + k + 1])
        return max(dp)

test = Solution()
print(test.longestIdealString(s = "acfgbd", k = 2))