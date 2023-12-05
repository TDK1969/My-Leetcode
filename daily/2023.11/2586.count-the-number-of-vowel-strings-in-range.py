"""
日期: 2023-11-07
题目: 统计范围内的元音字符串数
链接: https://leetcode-cn.com/problems/count-the-number-of-vowel-strings-in-range/
"""

from typing import *
from collections import *
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return len([1 for word in words[left:right + 1] if word[0] in "aeiou" and word[-1] in "aeiou"])