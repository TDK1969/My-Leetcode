"""
日期: 2024-01-17
题目: 字符频次唯一的最小删除次数
链接: https://leetcode-cn.com/problems/minimum-deletions-to-make-character-frequencies-unique/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minDeletions(self, s: str) -> int:
        c, res, has = Counter(s).values(), 0, set()
        for i in c:
            while i and i in has:
                i -= 1
                res += 1
            has.add(i)
        return res
                
print(Solution().minDeletions("ceabaacb"))
"""
--TESTCASE BEGIN--
TestCase 0: "aab"
TestCase 1: "aaabbbcc"
TestCase 2: "ceabaacb"
--TESTCASE END--
""" 
