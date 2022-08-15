"""
题目: 根据模式串构造最小数字
链接: https://leetcode-cn.com/problems/construct-smallest-number-from-di-string/
"""

from typing import *
from collections import *
from string import digits
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = list(digits[1:n + 2])
        i = j = 0
        while i < n:
            if pattern[i] == "I":
                i += 1
                continue
            else:
                j = i
                while j < n:
                    if pattern[j] == "D":
                        j += 1
                    else:
                        break
                ans[i:j + 1] = ans[i:j + 1][::-1]
                i = j
        return "".join(ans)

    def smallestNumber1(self, pattern: str) -> str:
        ans = []
        flag = False
        n = len(pattern)
        def dfs(i: int, t: int):
            nonlocal flag
            for j in range(1, n + 2):
                if j not in ans and (t == 0 or t == 1 and j > ans[-1] or t == 2 and j < ans[-1]):
                    ans.append(j)
                    if i == n:
                        flag = True
                        return
                    if pattern[i] == "I":
                        dfs(i + 1, 1)
                        if flag == True:
                            return
                    elif pattern[i] == "D":
                        dfs(i + 1, 2)
                        if flag == True:
                            return
                    ans.pop()
        dfs(0, 0)
        ans = [str(i) for i in ans]
        return "".join(ans)

test = Solution()
print(test.smallestNumber(pattern = "IIIDIDDD"))
