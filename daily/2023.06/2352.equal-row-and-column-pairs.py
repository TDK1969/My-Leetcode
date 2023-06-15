"""
日期: 2023-06-06
题目: 相等行列对
链接: https://leetcode-cn.com/problems/equal-row-and-column-pairs/
"""

from typing import *
from collections import *
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        n = len(grid)

        for i in range(n):
            r_t = ""
            c_t = ""
            for j in range(n):
                r_t += str(grid[i][j]) + " "
                c_t += str(grid[j][i]) + " "
            rows[r_t] += 1
            cols[c_t] += 1
        
        ans = 0
        for key in rows.keys() & cols.keys():
            ans += rows[key] * cols[key]
        
        return ans

test = Solution()
print(test.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
        