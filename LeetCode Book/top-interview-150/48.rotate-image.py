"""
日期: 2022-07-14
题目: 旋转图像
链接: https://leetcode-cn.com/problems/rotate-image/
"""

from typing import *
from collections import *
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 原地旋转,找规律
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                    matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]
    
test = Solution()
print(test.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))