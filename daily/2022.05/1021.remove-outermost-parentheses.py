"""
日期: 2022-05-28
题目: 删除最外层的括号
链接: https://leetcode-cn.com/problems/remove-outermost-parentheses/
"""

from typing import *
from collections import *
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        start = 0
        end = start + 1
        ans = ""
        cnt = 1

        while end < n:
            if s[end] == "(":
                cnt += 1
                end += 1
            elif s[end] == ")":
                cnt -= 1
                end += 1
            if cnt == 0:
                ans += s[start + 1:end - 1]
                start = end
                end = start + 1
                cnt = 1

        return ans

test = Solution()
print(test.removeOuterParentheses("(()())(())"))