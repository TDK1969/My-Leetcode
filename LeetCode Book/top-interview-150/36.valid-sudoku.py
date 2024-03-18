"""
日期: 2022-07-14
题目: 有效的数独
链接: https://leetcode-cn.com/problems/valid-sudoku/
"""

from typing import *
from collections import *
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols =  [set() for _ in range(9)]
        block = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                t = board[i][j]
                if t == ".":
                    continue
                else:
                    if t in rows[i] or t in cols[j] or t in block[(i // 3) * 3 + j // 3]:
                        return False
                    else:
                        rows[i].add(t)
                        cols[j].add(t)
                        block[(i // 3) * 3 + j // 3].add(t)
        return True