"""
日期: 2022-11-06
题目: 设计 Goal 解析器
链接: https://leetcode-cn.com/problems/goal-parser-interpretation/
"""

from typing import *
from collections import *
class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        i = 0
        ans = ""

        while i < n:
            if command[i] == "G":
                ans += "G"
                i += 1
            elif command[i] == "(" and command[i + 1] == ")":
                ans += "o"
                i += 2
            else:
                ans += "al"
                i += 4
        
        return ans
