"""
日期: 2023-02-13
题目: 替换子串得到平衡字符串
链接: https://leetcode-cn.com/problems/replace-the-substring-for-balanced-string/
"""

from typing import *
from collections import *
class Solution:
    def balancedString(self, s: str) -> int:
        cnt = [s.count("Q"), s.count("W"), s.count("E"), s.count("R")]
        
