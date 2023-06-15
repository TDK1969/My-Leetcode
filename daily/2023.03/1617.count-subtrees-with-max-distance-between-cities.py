"""
日期: 2023-03-12
题目: 统计子树中城市之间最大距离
链接: https://leetcode-cn.com/problems/count-subtrees-with-max-distance-between-cities/
"""

from typing import *
from collections import *
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]: