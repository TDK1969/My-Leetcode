"""
日期: 2022-07-14
题目: 有效的括号
链接: https://leetcode-cn.com/problems/valid-parentheses/
"""

from typing import *
from collections import *
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []

        for i in range(n):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            # 需要判断空栈的情况
            elif s[i] == ")" and (not stack or stack.pop() != "("):
                return False
            elif s[i] == "]" and (not stack or stack.pop() != "["):
                return False
            elif s[i] == "}" and (not stack or stack.pop() != "{"):
                return False
        return len(stack) == 0
            
                