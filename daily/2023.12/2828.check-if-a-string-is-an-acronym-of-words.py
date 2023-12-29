"""
日期: 2023-12-20
题目: 判别首字母缩略词
链接: https://leetcode-cn.com/problems/check-if-a-string-is-an-acronym-of-words/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for i in range(len(s)):
            if s[i] != words[i][0]:
                return False
        return True

"""
--TESTCASE BEGIN--
TestCase 0: ["alice","bob","charlie"],"abc"
TestCase 1: ["an","apple"],"a"
TestCase 2: ["never","gonna","give","up","on","you"],"ngguoy"
--TESTCASE END--
""" 

print(Solution().isAcronym(["never","gonna","give","up","on","you"],"ngguoy"))