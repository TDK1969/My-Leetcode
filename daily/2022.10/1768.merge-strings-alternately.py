"""
日期: 2022-10-23
题目: 交替合并字符串
链接: https://leetcode-cn.com/problems/merge-strings-alternately/
"""

from typing import *
from collections import *
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n = min(len(word1), len(word2))
        i = 0
        while i < n:
            ans += word1[i] + word2[i]
            i += 1
        if i < len(word1):
            ans += word1[i:]
        elif i < len(word2):
            ans += word2[i:]
        return ans

test = Solution()
print(test.mergeAlternately("123412341234", "abc"))