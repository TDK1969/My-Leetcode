"""
日期: 2022-10-20
题目: 第K个语法符号
链接: https://leetcode-cn.com/problems/k-th-symbol-in-grammar/
"""

from typing import *
from collections import *
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        t = bin(k - 1).count("1")
        return 1 if t & 1 else 0

test = Solution()
print(test.kthGrammar(5, 8))


        