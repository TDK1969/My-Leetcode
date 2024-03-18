"""
日期: 2023-11-01
题目: 整数转罗马数字
链接: https://leetcode-cn.com/problems/integer-to-roman/
"""

from typing import *
from collections import *
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        roman = [
            ["I", "V", "X"],
            ["X", "L", "C"],
            ["C", "D", "M"],
            ["M", "#", "#"]
        ]
        t = num
        i = 0
        while t:
            k = t % 10
            if k <= 3:
                ans = roman[i][0] * k + ans
            elif k == 4:
                ans = roman[i][0] + roman[i][1] + ans
            elif k <= 8:
                ans = roman[i][1] + roman[i][0] * (k - 5) + ans
            elif k == 9:
                ans = roman[i][0] + roman[i][2] + ans
            i += 1
            t = t // 10
        
        return ans

print(Solution().intToRoman(3999))