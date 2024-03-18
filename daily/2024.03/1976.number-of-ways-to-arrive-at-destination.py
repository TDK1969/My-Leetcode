"""
日期: 2024-03-05
题目: 到达目的地的方案数
链接: https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: 7,[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
TestCase 1: 2,[[1,0,10]]
--TESTCASE END--
""" 
