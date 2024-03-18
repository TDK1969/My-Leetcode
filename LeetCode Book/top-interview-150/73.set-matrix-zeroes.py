"""
日期: 2022-07-14
题目: 矩阵置零
链接: https://leetcode-cn.com/problems/set-matrix-zeroes/
"""

from typing import *
from collections import *
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        c = set()
        r = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        
        for i in r:
            for j in range(n):
                matrix[i][j] = 0
        
        for j in c:
            for i in range(m):
                matrix[i][j] = 0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        first_row_has_0 = False
        first_col_has_0 = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_has_0 = True
                    if j == 0:
                        first_col_has_0 = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        if first_row_has_0:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_has_0:
            for i in range(m):
                matrix[i][0] = 0

test = Solution()
print(test.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))