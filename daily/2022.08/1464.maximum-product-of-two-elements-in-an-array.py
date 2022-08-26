"""
日期: 2022-08-26
题目: 数组中两元素的最大乘积
链接: https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array/
"""

from typing import *
from collections import *
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p = 0
        q = 0

        for i in nums:
            if i >= p:
                q = p
                p = i
            elif i > q:
                q = i
        return (p - 1) * (q - 1)