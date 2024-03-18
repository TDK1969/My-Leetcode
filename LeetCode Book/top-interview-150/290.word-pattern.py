"""
日期: 2023-11-01
题目: 单词规律
链接: https://leetcode-cn.com/problems/word-pattern/
"""

from typing import *
from collections import *
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split(" ")
        if len(pattern) != len(word_list):
            return False

        s_d = defaultdict(str)
        t_d = defaultdict(str)

        for i in range(len(pattern)):
            if pattern[i] not in s_d and word_list[i] not in t_d:
                s_d[pattern[i]] = word_list[i]
                t_d[word_list[i]] = pattern[i]
            elif s_d[pattern[i]] != word_list[i] or t_d[word_list[i]] != pattern[i]:
                return False
        
        return True