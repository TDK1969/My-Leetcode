"""
日期: 2024-01-17
题目: 最大字符串配对数目
链接: https://leetcode.cn/problems/find-maximum-number-of-string-pairs/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        c = defaultdict(int)
        ans = 0
        for word in words:
            ans += c[word[::-1]]
            c[word] += 1
        return ans


"""
--TESTCASE BEGIN--
TestCase 0: ["cd","ac","dc","ca","zz"]
TestCase 1: ["ab","ba","cc"]
TestCase 2: ["aa","ab"]
--TESTCASE END--
""" 

print(Solution().maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))