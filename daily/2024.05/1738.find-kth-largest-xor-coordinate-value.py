"""
日期: 2024-05-26
题目: 找出第 K 大的异或坐标值
链接: https://leetcode.cn/problems/find-kth-largest-xor-coordinate-value/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = []
        preMatrix = [[0 for _ in range(n)] for _ in range(m)]
        preMatrix[0][0] = matrix[0][0]
        res.append(preMatrix[0][0])
        for i in range(1, n):
            preMatrix[0][i] = preMatrix[0][i - 1] ^ matrix[0][i]
            res.append(preMatrix[0][i])
        for i in range(1, m):
            preMatrix[i][0] = preMatrix[i - 1][0] ^ matrix[i][0]
            res.append(preMatrix[i][0])
        
        for i in range(1, m):
            for j in range(1, n):
                preMatrix[i][j] = preMatrix[i - 1][j] ^ preMatrix[i][j - 1] ^ preMatrix[i - 1][j - 1] ^ matrix[i][j]
                res.append(preMatrix[i][j])
        
        res.sort(reverse=True)
        return res[k - 1]

print(Solution().kthLargestValue([[5,2],[1,6]],2))

"""
--TESTCASE BEGIN--
TestCase 0: [[5,2],[1,6]],1
TestCase 1: [[5,2],[1,6]],2
TestCase 2: [[5,2],[1,6]],3
--TESTCASE END--
""" 
