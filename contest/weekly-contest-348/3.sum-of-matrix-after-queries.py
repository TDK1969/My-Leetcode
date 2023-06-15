"""
题目: 查询后矩阵的和
链接: https://leetcode-cn.com/problems/sum-of-matrix-after-queries/
"""

from typing import *
from collections import *

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        visited = [set(), set()]
        ans = 0

        for t, index, val in queries[::-1]:
            if index not in visited[t]:
                visited[t].add(index)
                ans += val * (n - len(visited[1 - t]))
        
        return ans

        
