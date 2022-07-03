"""
日期: 2022-07-01
题目: 为运算表达式设计优先级
链接: https://leetcode-cn.com/problems/different-ways-to-add-parentheses/
"""

from typing import *
from collections import *
import re
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        ans = []
        for i, c in enumerate(expression):
            if c in ["+", "-", "*"]:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:
                    for r in right:
                        if c == "+":
                            ans.append(l + r)
                        if c == "-":
                            ans.append(l - r)
                        if c == "*":
                            ans.append(l * r)
        return ans




        
        

test = Solution()
print(test.diffWaysToCompute(expression = "2-1-1"))