"""
日期: 2024-01-21
题目: 搜索二维矩阵
链接: https://leetcode-cn.com/problems/search-a-2d-matrix/
"""

from typing import *
from collections import *
from leetcode_utils import *
import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        indexs = [x[0] for x in matrix]
        i = bisect.bisect_right(indexs, target)
        if i == 0:
            return False
        j = bisect.bisect_left(matrix[i - 1], target)
        if j == len(matrix[i - 1]):
            return False
        return target == matrix[i - 1][j]

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],20))

"""
--TESTCASE BEGIN--
TestCase 0: [[1,3,5,7],[10,11,16,20],[23,30,34,60]],3
TestCase 1: [[1,3,5,7],[10,11,16,20],[23,30,34,60]],13
--TESTCASE END--
""" 
