"""
题目: 使数组变美的最小增量运算数
链接: https://leetcode-cn.com/problems/minimum-increment-operations-to-make-array-beautiful/
"""

from typing import *
from collections import *
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        incr_set = set()
        for i in range(len(nums) - 3):
            t = max(nums[i:i+3])
            if t < k:
                


