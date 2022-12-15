"""
日期: 2022-11-26
题目: 细分图中的可到达节点
链接: https://leetcode-cn.com/problems/reachable-nodes-in-subdivided-graph/
"""

from typing import *
from collections import *
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int: