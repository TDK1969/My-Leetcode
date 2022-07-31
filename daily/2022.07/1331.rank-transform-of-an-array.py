"""
日期: 2022-07-28
题目: 数组序号转换
链接: https://leetcode-cn.com/problems/rank-transform-of-an-array/
"""

from typing import *
from collections import *
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(arr)
        c = dict()
        r = 0
        for i, v in enumerate(nums):
            if v not in c:
                c[v] = i + r
            else:
                r -= 1
        for i, v in enumerate(arr):
            nums[i] = c[v] + 1
        return nums
