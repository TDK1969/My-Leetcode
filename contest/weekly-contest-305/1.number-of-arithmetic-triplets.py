"""
题目: 算术三元组的数目
链接: https://leetcode-cn.com/problems/number-of-arithmetic-triplets/
"""

from typing import *
from collections import *
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        s = set(nums)
        for i in nums:
            if i + diff in s and i + diff * 2 in s:
                ans += 1
        return ans