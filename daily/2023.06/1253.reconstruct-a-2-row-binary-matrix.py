"""
日期: 2023-06-29
题目: 重构 2 行二进制矩阵
链接: https://leetcode-cn.com/problems/reconstruct-a-2-row-binary-matrix/
"""

from typing import *
from collections import *
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]: