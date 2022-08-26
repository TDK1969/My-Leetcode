"""
日期: 2022-08-21
题目: 检查单词是否为句中其他单词的前缀
链接: https://leetcode-cn.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
"""

from typing import *
from collections import *
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ans = -1
        s = sentence.split(" ")
        l = len(searchWord)
        for i in range(len(s)):
            if s[i][:l] == searchWord:
                ans = i + 1
                break
        return ans
