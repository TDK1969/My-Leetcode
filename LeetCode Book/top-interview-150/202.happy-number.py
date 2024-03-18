"""
日期: 2023-11-01
题目: 快乐数
链接: https://leetcode-cn.com/problems/happy-number/
"""

from typing import *
from collections import *
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set([n])
        t = n
        while t != 1:
            x = t
            t = 0
            while x:
                t += (x % 10) ** 2
                x = x // 10
            if t in s:
                return False
            s.add(t)
        return True
