"""
日期: 2024-04-04
题目: 有向无环图中一个节点的所有祖先
链接: https://leetcode.cn/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

"""
--TESTCASE BEGIN--
TestCase 0: 8,[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
TestCase 1: 5,[[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
--TESTCASE END--
""" 
