"""
日期: 2022-07-14
题目: 括号生成
链接: https://leetcode-cn.com/problems/generate-parentheses/
"""

from typing import *
from collections import *
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(s: str, l: int, r: int):
            if l == r == n:
                ans.append(s)
            elif l < n:
                dfs(s + "(", l + 1, r)
            if l > r:
                dfs(s + ")", l, r + 1)
        dfs("", 0, 0)
        return ans


test = Solution()
print(test.generateParenthesis(4))