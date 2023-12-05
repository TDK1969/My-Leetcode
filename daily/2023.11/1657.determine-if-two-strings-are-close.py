"""
日期: 2023-11-30
题目: 确定两个字符串是否接近
链接: https://leetcode-cn.com/problems/determine-if-two-strings-are-close/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        if set(c1.keys()).difference(set(c2.keys())):
            return False

        return sorted(list(c1.values())) == sorted(list(c2.values()))
"""
--TESTCASE BEGIN--
TestCase 0: "abc","bca"
TestCase 1: "a","aa"
TestCase 2: "cabbba","abbccc"
--TESTCASE END--
""" 
print(Solution().closeStrings("abbzccca", "babzzczc"))