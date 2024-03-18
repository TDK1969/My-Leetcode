"""
日期: 2024-03-06
题目: 字符串解码
链接: https://leetcode-cn.com/problems/decode-string/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        stack1 = [""]
        stack2 = []
        for c in s:
            if c.

"""
--TESTCASE BEGIN--
TestCase 0: "3[a]2[bc]"
TestCase 1: "3[a2[c]]"
TestCase 2: "2[abc]3[cd]ef"
--TESTCASE END--
""" 
