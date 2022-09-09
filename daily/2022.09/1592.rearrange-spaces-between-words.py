"""
日期: 2022-09-07
题目: 重新排列单词间的空格
链接: https://leetcode-cn.com/problems/rearrange-spaces-between-words/
"""

from typing import *
from collections import *
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        space_cnt = text.count(" ")
        if len(words) == 1:
            return words[0] + " " * space_cnt
        gap_space = space_cnt // (len(words) - 1)
        gap_space_str = " " * gap_space
        tail_space = space_cnt - (len(words) - 1) * gap_space

        ans = ""
        for index, word in enumerate(words):
            ans += word
            if index != len(words) - 1:
                ans += gap_space_str
        ans += " " * tail_space
        return ans

t = Solution()
print(t.reorderSpaces("  this   is  a sentence "))