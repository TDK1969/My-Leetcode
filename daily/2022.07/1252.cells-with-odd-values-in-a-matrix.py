"""
日期: 2022-07-12
题目: 奇数值单元格的数目
链接: https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix/
"""

from typing import *
from collections import *
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        r = 0
        c = 0


        for x, y in indices:
            r = r ^ (1 << x)
            c = c ^ (1 << y)
            
        oddx = 0
        oddy = 0

        while r:
            oddx += r & 1
            r = r >> 1
        
        while c:
            oddy += c & 1
            c = c >> 1

        return oddx * (n - oddy) + oddy * (m - oddx)

test = Solution()
print(test.oddCells(m = 2, n = 2, indices = [[1,1],[0,0]]))

