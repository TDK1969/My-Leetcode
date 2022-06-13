"""
日期: 2022-06-12
题目: 查找和替换模式
链接: https://leetcode-cn.com/problems/find-and-replace-pattern/
"""

from typing import *
from collections import *
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p = set(pattern)

        ans = []
        for word in words:
            mapping = set(zip(word, pattern))
            if len(mapping) == len(p) and len(mapping) == len(set(word)):
                ans.append(word)
        return ans