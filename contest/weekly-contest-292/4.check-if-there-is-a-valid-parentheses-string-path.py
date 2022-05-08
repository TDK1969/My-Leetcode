"""
题目: 检查是否有合法括号字符串路径
链接: https://leetcode-cn.com/problems/check-if-there-is-a-valid-parentheses-string-path/
"""

from typing import *
from collections import *

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] != "(" or grid[m - 1][n - 1] != ")" or (m + n - 1) & 1:
            return False
        
        def dfs(x: int, y: int, c: int) -> bool:
            if m + n - x - y - 1 < c:
                return False
            if x == m - 1 and y == n - 1:
                return c == 1
            c += 1 if grid[x][y] == "(" else -1
            return c >= 0 and (x + 1 < m and dfs(x + 1, y, c) or y + 1 < n and dfs(x, y + 1, c))
        
        return dfs(0, 0, 0)
        
        

test = Solution()
print(test.hasValidPath([["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]))

            

                