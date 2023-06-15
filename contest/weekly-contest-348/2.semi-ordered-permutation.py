"""
题目: 半有序排列
链接: https://leetcode-cn.com/problems/semi-ordered-permutation/
"""

from typing import *
from collections import *
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                p1 = i
            elif nums[i] == n:
                p2 = i
        
        return p1 + n - p2 - 1 - (1 if p1 > p2 else 0)