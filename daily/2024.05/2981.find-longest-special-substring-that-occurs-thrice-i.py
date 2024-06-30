"""
日期: 2024-05-29
题目: 找出出现至少三次的最长特殊子字符串 I
链接: https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maximumLength(self, s: str) -> int:
        cnt = [[0 for _ in range(51)] for _ in range(26)]
        left, right = 0, 0
        n = len(s)
        ans = -1
        while right <= n:
            if right == n or s[left] != s[right]:
                l = right - left
                for i in range(1, l + 1):
                    cnt[ord(s[left]) - 97][i] += l - i + 1
                    if cnt[ord(s[left]) - 97][i] >= 3 and i > ans:
                        ans = i
                left = right

            right += 1
        return ans

print(Solution().maximumLength("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
"""
--TESTCASE BEGIN--
TestCase 0: "aaaa"
TestCase 1: "abcdef"
TestCase 2: "abcaba"
--TESTCASE END--
""" 
