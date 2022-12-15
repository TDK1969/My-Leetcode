"""
日期: 2022-11-14
题目: 数组的均值分割
链接: https://leetcode-cn.com/problems/split-array-with-same-average/
"""

from typing import *
from collections import *
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = sum(nums) / n
        