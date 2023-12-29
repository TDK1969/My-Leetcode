"""
日期: 2023-12-13
题目: 字典序最小回文串
链接: https://leetcode-cn.com/problems/lexicographically-smallest-palindrome/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = list(s)
        p, q = 0, len(l) - 1
        while p < q:
            if l[p] != l[q]:
                l[p] = l[q] = min(l[p], l[q])
            p += 1
            q -= 1
        return "".join(l)

"""
--TESTCASE BEGIN--
TestCase 0: "egcfe"
TestCase 1: "abcd"
TestCase 2: "seven"
--TESTCASE END--
""" 
print(Solution().makeSmallestPalindrome("seven"))