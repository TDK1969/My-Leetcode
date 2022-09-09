"""
题目: 被列覆盖的最多行数
链接: https://leetcode-cn.com/problems/maximum-rows-covered-by-columns/
"""

from typing import *
from collections import *

class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        need_cols = [set() for _ in range(len(mat))]
        has_one_cols = set()
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    need_cols[i].add(j)
                    has_one_cols.add(j)

        visited = set()
        has_one_cols = list(has_one_cols)
        p = len(has_one_cols)
        ans = 0

        def dfs(k: int):
            for i in range(k, n):
                if i not in visited:
                    visited.add(i)

                    t = 0
                    for j in need_cols:
                        if j.issubset(visited):
                            t += 1
                    nonlocal ans
                    if t > ans:
                        ans = t
                    
                    if len(visited) < cols:
                        dfs(i + 1)
                    
                    visited.remove(i)
        dfs(0)
        return ans

test = Solution()
print(test.maximumRows(mat = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], cols = 2))
                
                    
                        






        