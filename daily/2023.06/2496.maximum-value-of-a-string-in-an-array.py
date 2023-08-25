"""
日期: 2023-06-23
题目: 数组中字符串的最大值
链接: https://leetcode-cn.com/problems/maximum-value-of-a-string-in-an-array/
"""

from typing import *
from collections import *
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        strs.sort(key=lambda x:int(x) if x.isdigit() else len(x))
        return int(strs[-1]) if strs[-1].isdigit() else len(strs[-1])

test = Solution()
print(test.maximumValue(["alic3","bob","3","4","00000"]))