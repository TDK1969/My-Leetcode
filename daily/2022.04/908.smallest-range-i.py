"""
日期: 2022-04-30
题目: 最小差值 I
链接: https://leetcode-cn.com/problems/smallest-range-i/
"""
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(max(nums) - min(nums) - 2 * k, 0)      