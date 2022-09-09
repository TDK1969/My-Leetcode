"""
日期: 2022-09-04
题目: 二进制矩阵中的特殊位置
链接: https://leetcode-cn.com/problems/special-positions-in-a-binary-matrix/
"""

from typing import *
from collections import *
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r = len(mat)
        c = len(mat[0])
        ans = 0
        one_r = [0 for _ in range(r)]
        one_c = [0 for _ in range(c)]
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    one_r[i] += 1
                    one_c[j] += 1
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1 and one_r[i] == 1 and one_c[j] == 1:
                    ans += 1
        return ans

test = Solution()
print(test.numSpecial([[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]))


                    