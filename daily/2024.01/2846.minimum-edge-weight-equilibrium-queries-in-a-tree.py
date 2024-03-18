"""
日期: 2024-01-26
题目: 边权重均等查询
链接: https://leetcode.cn/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

"""
--TESTCASE BEGIN--
TestCase 0: 7,[[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]],[[0,3],[3,6],[2,6],[0,6]]
TestCase 1: 8,[[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]],[[4,6],[0,4],[6,5],[7,4]]
--TESTCASE END--
""" 
