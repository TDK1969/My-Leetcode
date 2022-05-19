"""
日期: 2022-05-19
题目: 最少移动次数使数组元素相等 II
链接: https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/
"""

from typing import *
from collections import *
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # 可通过数学证明,中位数是最优
        nums.sort()
        n = len(nums)
        mid = nums[n // 2]
        ans = 0
        for num in nums:
            ans += abs(num - mid)
        return ans