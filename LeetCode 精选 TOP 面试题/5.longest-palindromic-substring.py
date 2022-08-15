"""
日期: 2022-07-14
题目: 最长回文子串
链接: https://leetcode-cn.com/problems/longest-palindromic-substring/
"""

from typing import *
from collections import *
from wsgiref.headers import tspecials
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend(left: int, right: int) -> int:
            n = len(s)
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        ans = 0
        ans_s = ""
        for i in range(len(s)):
            t1 = extend(i, i)
            t2 = extend(i, i + 1)
            if t1 > ans:
                ans = t1
                ans_s = s[i - t1 // 2:i + t1 // 2 + 1]
            if t2 > ans:
                ans = t2
                ans_s = s[i - t2 // 2 + 1:i + t2 // 2 + 1]
        return ans_s

test = Solution()
print(test.longestPalindrome("cbbd"))
