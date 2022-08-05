"""
日期: 2022-08-03
题目: 有序队列
链接: https://leetcode-cn.com/problems/orderly-queue/
"""

from typing import *
from collections import *
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k != 1:
            return "".join(sorted(list(s)))
        else:
            ans = s
            for _ in range(len(s)):
                ans = min(ans, s)
                s = s[1:] + s[0]
            return ans