"""
日期: 2024-11-15
题目: 最少翻转次数使二进制矩阵回文 I
链接: https://leetcode.cn/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt1 = cnt2 = 0
        for i in range(m):
            for j in range(n // 2):
                if grid[i][j] != grid[i][n - j - 1]:
                    cnt1 += 1
        
        for i in range(n):
            for j in range(m // 2):
                if grid[j][i] != grid[m - 1 - j][i]:
                    cnt2 += 1
        
        return min(cnt1, cnt2)
        

            

        

"""
--TESTCASE BEGIN--
TestCase 0: [[1,0,0],[0,0,0],[0,0,1]]
TestCase 1: [[0,1],[0,1],[0,0]]
TestCase 2: [[1],[0]]
--TESTCASE END--
""" 
