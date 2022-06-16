"""
日期: 2022-06-16
题目: 数组中的 k-diff 数对
链接: https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/
"""

from typing import *
from collections import *
import bisect
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        visited = set()
        ans = 0
        for i, v in enumerate(nums):
            d = bisect.bisect_left(nums, k + v)
            if d != i and d < len(nums) and k + v == nums[d] and v not in visited:
                visited.add(v)
                ans += 1
        return ans