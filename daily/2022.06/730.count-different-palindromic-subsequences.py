"""
日期: 2022-06-10
题目: 统计不同回文子序列
链接: https://leetcode-cn.com/problems/count-different-palindromic-subsequences/
"""

from typing import *
from collections import *
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for