"""
日期: 2022-07-14
题目: 字符串转换整数 (atoi)
链接: https://leetcode-cn.com/problems/string-to-integer-atoi/
"""

from typing import *
from collections import *
class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        s = s.lstrip()
        flag = s[0] == "-"
        nums = "0123456789"
        boundary = (1 << 31) - (0 if flag else 1)
        ans = 0
        cnt = 1 if s[0] == "-" or s[0] == "+" else 0
        for i in range(cnt, len(s)):
            if s[i] not in nums:
                break
            t = ord(s[i]) - ord("0")
            if boundary - ans * 10 < t:
                ans = boundary
                break
            else:
                ans = ans * 10 + t
        return -ans if flag else ans

test = Solution()
print(test.myAtoi("  -42"))
            
            
            