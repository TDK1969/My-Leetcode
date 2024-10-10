"""
日期: 2024-06-29
题目: 移除字符串中的尾随零
链接: https://leetcode.cn/problems/remove-trailing-zeros-from-a-string/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n = len(num)
        ans = []
        for i in range(n - 1, -1, -1):
            if num[i] == "0" and len(ans) == 0:
                continue
            else:
                ans.append(num[i])
        return "".join(reversed(ans))

"""
--TESTCASE BEGIN--
TestCase 0: "51230100"
TestCase 1: "123"
--TESTCASE END--
""" 
