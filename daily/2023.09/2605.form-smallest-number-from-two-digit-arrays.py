"""
日期: 2023-09-05
题目: 从两个数字数组里生成最小数字
链接: https://leetcode-cn.com/problems/form-smallest-number-from-two-digit-arrays/
"""

from typing import *
from collections import *
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(1, 10):
            if i in nums1 and i in nums2:
                return i
        a, b = min(nums1), min(nums2)
        return min(a * 10 + b, b * 10 + a)