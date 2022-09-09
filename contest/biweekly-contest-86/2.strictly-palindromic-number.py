"""
题目: 严格回文的数字
链接: https://leetcode-cn.com/problems/strictly-palindromic-number/
"""

from typing import *
from collections import *

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def change(k: int) -> bool:
            t = n
            s = []
            while t:
                s.append(t % k)
                t = t // k
            return s == s[::-1]
        
        for k in range(2, n - 1):
            if not change(k):
                return False
        return True

        