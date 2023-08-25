"""
题目: 最大字符串配对数目
链接: https://leetcode-cn.com/problems/find-maximum-number-of-string-pairs/
"""

from typing import *
from collections import *
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        words_set = set(words)
        ans = 0
        for i in words:
            if i != i[::-1] and i[::-1] in words_set:
                ans += 1
        
        return ans // 2