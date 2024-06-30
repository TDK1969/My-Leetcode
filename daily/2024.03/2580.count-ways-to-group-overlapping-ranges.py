"""
日期: 2024-03-27
题目: 统计将重叠区间合并成组的方案数
链接: https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [[6,10],[5,15]]
TestCase 1: [[1,3],[10,20],[2,5],[4,8]]
--TESTCASE END--
""" 
