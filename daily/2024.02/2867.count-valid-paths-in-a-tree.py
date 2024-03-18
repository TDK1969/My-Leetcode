"""
日期: 2024-02-27
题目: 统计树中的合法路径数目
链接: https://leetcode.cn/problems/count-valid-paths-in-a-tree/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: 5,[[1,2],[1,3],[2,4],[2,5]]
TestCase 1: 6,[[1,2],[1,3],[2,4],[3,5],[3,6]]
--TESTCASE END--
""" 
