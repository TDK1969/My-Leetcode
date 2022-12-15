"""
日期: 2022-11-13
题目: 自定义字符串排序
链接: https://leetcode-cn.com/problems/custom-sort-string/
"""

from typing import *
from collections import *
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        a = defaultdict(int)
        for index, alpha in enumerate(order):
            a[alpha] = index
        s = sorted(list(s), key=lambda x:a[x])
        return "".join(s)

test = Solution()
print(test.customSortString(order = "cba", s = "abcd"))

