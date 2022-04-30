"""
题目: 统计是给定字符串前缀的字符串数目
链接: https://leetcode-cn.com/problems/count-prefixes-of-a-given-string/
"""
from typing import *
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for word in words:
            if word == s[:len(word)]:
                ans += 1
        return ans