"""
日期: 2022-05-12
题目: 删列造序
链接: https://leetcode-cn.com/problems/delete-columns-to-make-sorted/
"""

from typing import *
from collections import *
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        col = [True for _ in range(n)]
        ans = 0

        for i in range(1, len(strs)):
            for j in range(n):
                if col[j] and strs[i][j] < strs[i - 1][j]:
                    col[j] = False
                    ans += 1
        
        return ans

