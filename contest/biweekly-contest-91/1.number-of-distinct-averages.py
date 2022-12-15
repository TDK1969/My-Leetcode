"""
题目: 不同的平均值数目
链接: https://leetcode-cn.com/problems/number-of-distinct-averages/
"""

from typing import *
from collections import *

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        ans = set()
        i, j = 0, len(nums) - 1
        while i < j:
            ans.add((nums[i] + nums[j]) / 2)
            i += 1
            j -= 1
        return len(ans)
