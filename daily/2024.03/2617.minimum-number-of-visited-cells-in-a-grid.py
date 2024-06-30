"""
日期: 2024-03-22
题目: 网格图中最少访问的格子数
链接: https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
TestCase 1: [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
TestCase 2: [[2,1,0],[1,0,0]]
--TESTCASE END--
""" 
