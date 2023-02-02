"""
日期: 2022-12-19
题目: 寻找图中是否存在路径
链接: https://leetcode-cn.com/problems/find-if-path-exists-in-graph/
"""

from typing import *
from collections import *
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool: