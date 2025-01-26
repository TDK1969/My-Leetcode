"""
日期: 2024-12-26
题目: 字符串及其反转中是否存在同一子字符串
链接: https://leetcode.cn/problems/existence-of-a-substring-in-a-string-and-its-reverse/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        word_set = set()
        n = len(s)
        for i in range(n - 1):
            word_set.add(s[i:i + 2])
        
        for i in range(n - 1):
            if s[i + 1] + s[i] in word_set:
                return True

        return False

print(Solution().isSubstringPresent("abcd"))

"""
--TESTCASE BEGIN--
TestCase 0: "leetcode"
TestCase 1: "abcba"
TestCase 2: "abcd"
--TESTCASE END--
""" 
