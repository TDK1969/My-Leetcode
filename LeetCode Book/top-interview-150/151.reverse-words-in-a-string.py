"""
日期: 2023-11-01
题目: 反转字符串中的单词
链接: https://leetcode-cn.com/problems/reverse-words-in-a-string/
"""

from typing import *
from collections import *
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i for i in s.strip().split(" ") if i][::-1])

print(Solution().reverseWords("a good   example"))