"""
日期: 2024-12-04
题目: 棋盘上有效移动组合的数目
链接: https://leetcode.cn/problems/number-of-valid-move-combinations-on-chessboard/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        

"""
--TESTCASE BEGIN--
TestCase 0: ["rook"],[[1,1]]
TestCase 1: ["queen"],[[1,1]]
TestCase 2: ["bishop"],[[4,3]]
--TESTCASE END--
""" 
