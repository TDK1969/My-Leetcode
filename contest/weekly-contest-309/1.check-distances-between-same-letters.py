"""
题目: 检查相同字母间的距离
链接: https://leetcode-cn.com/problems/check-distances-between-same-letters/
"""

from typing import *
from collections import *

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = dict()
        n = len(s)
        for i in range(n):
            k = ord(s[i]) - ord("a")
            if k not in d:
                d[k] = i
            else:
                d[k] = i - d[k] - 1
        
        for i in range(len(distance)):
            if i in d and d[i] != distance[i]:
                return False
        return True