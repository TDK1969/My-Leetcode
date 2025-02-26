"""
日期: 2024-07-07
题目: 检查操作是否合法
链接: https://leetcode.cn/problems/check-if-move-is-legal/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:

"""
--TESTCASE BEGIN--
TestCase 0: [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]],4,3,"B"
TestCase 1: [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]],4,4,"W"
--TESTCASE END--
""" 
