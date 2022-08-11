"""
日期: 2022-08-11
题目: 重新格式化字符串
链接: https://leetcode-cn.com/problems/reformat-the-string/
"""

from typing import *
from collections import *
class Solution:
    def reformat(self, s: str) -> str:
        d = []
        a = []
        for i in s:
            if ord("0") <= ord(i) <= ord("9"):
                d.append(i)
            else:
                a.append(i)
        if abs(len(d) - len(a)) > 1:
            return ""
        ans = ""
        i, j = 0, 0
        while i < len(d) and j < len(a):
            ans += d[i] + a[j]
            i += 1
            j += 1
        if j == len(a) and i < len(d):
            ans += d[i]
        if i == len(d) and j < len(a):
            ans = a[j] + ans
        return ans