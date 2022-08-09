"""
日期: 2022-08-08
题目: 特殊的二进制序列
链接: https://leetcode-cn.com/problems/special-binary-string/
"""

from typing import *
from collections import *
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        segments = []
        left = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] == "1":
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    segments.append("1" + self.makeLargestSpecial(s[left + 1:i]) + "0")
                    left = i + 1
        segments.sort(reverse=True)
        return "".join(segments)