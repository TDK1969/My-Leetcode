"""
日期: 2024-06-25
题目: 找到矩阵中的好子集
链接: https://leetcode.cn/problems/find-a-good-subset-of-the-matrix/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:

"""
--TESTCASE BEGIN--
TestCase 0: [[0,1,1,0],[0,0,0,1],[1,1,1,1]]
TestCase 1: [[0]]
TestCase 2: [[1,1,1],[1,1,1]]
--TESTCASE END--
""" 
