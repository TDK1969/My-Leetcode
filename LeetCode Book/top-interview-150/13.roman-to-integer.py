"""
日期: 2022-07-14
题目: 罗马数字转整数
链接: https://leetcode-cn.com/problems/roman-to-integer/
"""

from typing import *
from collections import *
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n = len(s)
        for i in range(n):
            if s[i] in ["V", "L", "D", "M"]:
                ans += d[s[i]]
            elif s[i] == "I":
                if i + 1 < n and s[i + 1] in ["V", "X"]:
                    ans -= 1
                else:
                    ans += 1
            elif s[i] == "X":
                if i + 1 < n and s[i + 1] in ["L", "C"]:
                    ans -= 10
                else:
                    ans += 10
            elif s[i] == "C":
                if i + 1 < n and s[i + 1] in ["D", "M"]:
                    ans -= 100
                else:
                    ans += 100
        return ans

t = Solution()
print(t.romanToInt("MCMXCIV"))