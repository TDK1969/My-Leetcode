"""
日期: 2024-08-10
题目: 找到 Alice 和 Bob 可以相遇的建筑
链接: https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:

"""
--TESTCASE BEGIN--
TestCase 0: [6,4,8,5,2,7],[[0,1],[0,3],[2,4],[3,4],[2,2]]
TestCase 1: [5,3,8,2,6,1,4,6],[[0,7],[3,5],[5,2],[3,0],[1,6]]
--TESTCASE END--
""" 
