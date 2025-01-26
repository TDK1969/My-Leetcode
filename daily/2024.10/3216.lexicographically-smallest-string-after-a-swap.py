"""
日期: 2024-10-30
题目: 交换后字典序最小的字符串
链接: https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def getSmallestString(self, s: str) -> str:
        l = list(s)
        n = len(l)
        for i in range(n - 1):
            if int(l[i]) & 1 == int(l[i + 1]) & 1 and int(l[i]) > int(l[i + 1]):
                l[i], l[i + 1] = l[i + 1], l[i]
                break
        return "".join(l)

print(Solution().getSmallestString("45320"))

"""
--TESTCASE BEGIN--
TestCase 0: "45320"
TestCase 1: "001"
--TESTCASE END--
""" 
