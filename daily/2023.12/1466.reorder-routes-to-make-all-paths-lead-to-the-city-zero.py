"""
日期: 2023-12-07
题目: 重新规划路线
链接: https://leetcode-cn.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: 6,[[0,1],[1,3],[2,3],[4,0],[4,5]]
TestCase 1: 5,[[1,0],[1,2],[3,2],[3,4]]
TestCase 2: 3,[[1,0],[2,0]]
--TESTCASE END--
""" 
