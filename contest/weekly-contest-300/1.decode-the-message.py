"""
题目: 解密消息
链接: https://leetcode-cn.com/problems/decode-the-message/
"""

from curses.ascii import SO
from typing import *
from collections import *

from sortedcontainers import SortedKeyList
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        i = 0
        for c in key:
            if c != " " and c not in d.keys():
                d[c] = chr(ord("a") + i)
                i += 1

        ans = ""
        for i in message:
            if i == " ":
                ans += " "
            else:
                ans += d[i]
        return ans


test = Solution()
print(test.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"))
