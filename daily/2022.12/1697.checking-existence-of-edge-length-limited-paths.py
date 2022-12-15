"""
日期: 2022-12-14
题目: 检查边长度限制的路径是否存在
链接: https://leetcode-cn.com/problems/checking-existence-of-edge-length-limited-paths/
"""

from typing import *
from collections import *
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]: