"""
日期: 2025-01-09
题目: 统计重新排列后包含另一个字符串的子字符串数目 I
链接: https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        

"""
--TESTCASE BEGIN--
TestCase 0: "bcca","abc"
TestCase 1: "abcabc","abc"
TestCase 2: "abcabc","aaabc"
--TESTCASE END--
""" 
