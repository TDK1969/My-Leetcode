"""
日期: 2024-01-20
题目: 按分隔符拆分字符串
链接: https://leetcode.cn/problems/split-strings-by-separator/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

"""
--TESTCASE BEGIN--
TestCase 0: ["one.two.three","four.five","six"],"."
TestCase 1: ["$easy$","$problem$"],"$"
TestCase 2: ["|||"],"|"
--TESTCASE END--
""" 
