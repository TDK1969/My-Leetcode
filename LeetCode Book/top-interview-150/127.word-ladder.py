"""
日期: 2024-01-18
题目: 单词接龙
链接: https://leetcode-cn.com/problems/word-ladder/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
"""
--TESTCASE BEGIN--
TestCase 0: "hit","cog",["hot","dot","dog","lot","log","cog"]
TestCase 1: "hit","cog",["hot","dot","dog","lot","log"]
--TESTCASE END--
""" 
