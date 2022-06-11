"""
题目: 强密码检验器 II
链接: https://leetcode-cn.com/problems/strong-password-checker-ii/
"""

from typing import *
from collections import *

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        lower = False
        upper = False
        digit = False
        code = False

        codes = "!@#$%^&*()-+"

        if len(password) < 8:
            return False

        for i, c in enumerate(password):
            if c.islower():
                lower = True
            elif c.isupper():
                upper = True
            elif c.isdigit():
                digit = True
            elif c in codes:
                code = True
            
            if i > 0 and password[i] == password[i - 1]:
                return False
        
        return lower and upper and digit and code
        