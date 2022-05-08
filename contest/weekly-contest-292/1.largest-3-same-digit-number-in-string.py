"""
题目: 字符串中最大的 3 位相同数字
链接: https://leetcode-cn.com/problems/largest-3-same-digit-number-in-string/
"""

from typing import *
from collections import *

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = ""
        for i in range(n - 2):
            if num[i] == num[i + 1] == num[i + 2] and num[i:i + 3] > ans:
                ans = num[i:i + 3]
        return ans

