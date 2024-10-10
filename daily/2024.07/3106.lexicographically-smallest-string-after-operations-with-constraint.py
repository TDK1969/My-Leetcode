"""
日期: 2024-07-27
题目: 满足距离约束且字典序最小的字符串
链接: https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:

"""
--TESTCASE BEGIN--
TestCase 0: "zbbz",3
TestCase 1: "xaxcd",4
TestCase 2: "lol",0
--TESTCASE END--
""" 
