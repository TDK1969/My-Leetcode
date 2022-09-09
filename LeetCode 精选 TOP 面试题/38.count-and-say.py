"""
日期: 2022-07-14
题目: 外观数列
链接: https://leetcode-cn.com/problems/count-and-say/
"""

from typing import *
from collections import *
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        nxt_s = ""

        for _ in range(n - 1):
            l = r = 0
            while r < len(s):
                while r < len(s) and s[l] == s[r]:
                    r += 1
                nxt_s += f"{r - l}{s[l]}"
                l = r
            
            s = nxt_s[:]
            nxt_s = ""
        return s

test = Solution()
print(test.countAndSay(5))