"""
日期: 2024-09-24
题目: 字符串中最多数目的子序列
链接: https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: "abdcdbc","ac"
TestCase 1: "aabb","ab"
--TESTCASE END--
""" 
