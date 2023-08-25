"""
题目: 字符串连接删减字母
链接: https://leetcode-cn.com/problems/decremental-string-concatenation/
"""

from typing import *
from collections import *
class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        ans = words[0]
        n = len(words)
        for i in range(1, n):
            if ans[-1] == words[0]