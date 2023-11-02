"""
日期: 2023-11-01
题目: 同构字符串
链接: https://leetcode-cn.com/problems/isomorphic-strings/
"""

from typing import *
from collections import *
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_d = dict()
        t_d = dict()

        for i in range(len(s)):
            if s[i] not in s_d and t[i] not in t_d:
                s_d[s[i]] = t[i]
                t_d[t[i]] = s[i]
            elif s_d[s[i]] != t[i] or t_d[t[i]] != s[i]:
                return False
        
        return True