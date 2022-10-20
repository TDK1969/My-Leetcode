"""
题目: 与对应负数同时存在的最大正整数
链接: https://leetcode-cn.com/problems/largest-positive-integer-that-exists-with-its-negative/
"""

from typing import *
from collections import *
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a = set(nums)
        ans = -1
        for i in a:
            if i > 0 and -i in a and i > ans:
                ans = i
        return i
