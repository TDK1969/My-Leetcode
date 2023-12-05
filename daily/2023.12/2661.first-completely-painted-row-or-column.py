"""
日期: 2023-12-01
题目: 找出叠涂元素
链接: https://leetcode-cn.com/problems/first-completely-painted-row-or-column/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        d = {}
        m, n = len(mat), len(mat[0])
        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                d[mat[i][j]] = (i, j)
        
        for k in range(len(arr)):
            x, y = d[arr[k]]
            rows[x] += 1
            cols[y] += 1
            if rows[x] == n or cols[y] == m:
                return k

"""
--TESTCASE BEGIN--
TestCase 0: [1,3,4,2],[[1,4],[2,3]]
TestCase 1: [2,8,7,4,1,3,5,6,9],[[3,2,5],[1,4,6],[8,7,9]]
--TESTCASE END--
""" 

print(Solution().firstCompleteIndex([2,8,7,4,1,3,5,6,9],[[3,2,5],[1,4,6],[8,7,9]]))