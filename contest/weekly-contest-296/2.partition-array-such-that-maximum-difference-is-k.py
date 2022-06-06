"""
题目: 划分数组使最大差为 K
链接: https://leetcode-cn.com/problems/partition-array-such-that-maximum-difference-is-k/
"""

from typing import *
from collections import *

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        i = 0
        j = -1
        while i < len(nums):
            j = i
            i += 1
            while i < len(nums):
                if nums[i] - nums[j] <= k:
                    i += 1
                else:
                    break
            cnt += 1
        return cnt

