"""
日期: 2023-02-23
题目: 循环码排列
链接: https://leetcode-cn.com/problems/circular-permutation-in-binary-representation/
"""

from typing import *
from collections import *
class Solution:
    # 89. 格雷编码 官方题解
    def grayCode(self, n: int) -> List[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i
        return ans

    def circularPermutation(self, n: int, start: int) -> List[int]:
        p = self.grayCode(n) * 2
        for i, x in enumerate(p):
            if x == start:
                return p[i:len(p) // 2 + i]