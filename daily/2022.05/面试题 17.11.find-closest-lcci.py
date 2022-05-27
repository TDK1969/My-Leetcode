"""
日期: 2022-05-27
题目: 单词距离
链接: https://leetcode-cn.com/problems/find-closest-lcci/
"""

import enum
from typing import *
from collections import *
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        start = -100000
        end = 100000
        min_close = float("inf")

        for index, word in enumerate(words):
            if word == word1:
                start = index
                min_close = min(min_close, abs(end - start))
            if word == word2:
                end = index
                min_close = min(min_close, abs(end - start))
        
        return min_close
