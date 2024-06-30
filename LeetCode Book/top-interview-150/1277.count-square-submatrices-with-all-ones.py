"""
日期: 2024-03-21
题目: 统计全为 1 的正方形子矩阵
链接: https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maximalSquare(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        ans = 0
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = matrix[i][0]
            ans = max(ans, dp[i][0])
        for j in range(m):
            dp[0][j] = matrix[0][j]
            ans = max(ans, dp[0][j])
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ans = max(ans, dp[i][j])
    
        return ans ** 2

print(Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))    

"""
--TESTCASE BEGIN--
TestCase 0: [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
TestCase 1: [[1,0,1],[1,1,0],[1,1,0]]
--TESTCASE END--
""" 
