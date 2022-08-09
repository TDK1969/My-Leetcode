"""
日期: 2022-08-06
题目: 数组中的字符串匹配
链接: https://leetcode-cn.com/problems/string-matching-in-an-array/
"""

from typing import *
from collections import *
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort()
        ans = set()
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    ans.add(words[i])
                    break
        return list(ans)