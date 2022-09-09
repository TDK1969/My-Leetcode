"""
日期: 2022-09-06
题目: 统计子串中的唯一字符
链接: https://leetcode-cn.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
"""

from typing import *
from collections import *
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = collections.defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)

        res = 0
        for arr in index.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res