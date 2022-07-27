"""
题目: 第一个出现两次的字母
链接: https://leetcode-cn.com/problems/first-letter-to-appear-twice/
"""

from typing import *
from collections import *
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = set()
        for alpha in s:
            if alpha not in d:
                d.add(alpha)
            else:
                return alpha