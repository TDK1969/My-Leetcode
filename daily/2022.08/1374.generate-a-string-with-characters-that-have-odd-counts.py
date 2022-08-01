"""
日期: 2022-08-01
题目: 生成每种字符都是奇数个的字符串
链接: https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts/
"""

from typing import *
from collections import *
class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * (n - (1 - n & 1)) + "b" * (1 - n & 1)