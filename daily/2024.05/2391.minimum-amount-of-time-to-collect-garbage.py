"""
日期: 2024-05-11
题目: 收集垃圾的最少总时间
链接: https://leetcode.cn/problems/minimum-amount-of-time-to-collect-garbage/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: ["G","P","GP","GG"],[2,4,3]
TestCase 1: ["MMM","PGM","GP"],[3,10]
--TESTCASE END--
""" 
