"""
日期: 2023-06-13
题目: 数组中不等三元组的数目
链接: https://leetcode-cn.com/problems/number-of-unequal-triplets-in-array/
"""

from typing import *
from collections import *
import bisect
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        i = 0
        ans = 0

        while i < n:
            l = bisect.bisect_left(nums, nums[i])
            r = bisect.bisect_right(nums, nums[i])
            ans += l * (r - l) * (n - r)
            i = r

        return ans


test = Solution()
print(test.unequalTriplets([4,4,2,4,3]))
