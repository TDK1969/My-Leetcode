"""
题目: 相等行列对
链接: https://leetcode-cn.com/problems/equal-row-and-column-pairs/
"""

from typing import *
from collections import *
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        r_counter = defaultdict(int)
        c_counter = defaultdict(int)

        for i in grid:
            r_counter[tuple(i)] += 1
        
        for j in range(n):
            c_counter[tuple([grid[i][j] for i in range(n)])] += 1
        
        ans = 0
        for k in r_counter.keys() & c_counter.keys():
            ans += r_counter[k] * c_counter[k]
        
        return ans
        

test = Solution()
print(test.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]))