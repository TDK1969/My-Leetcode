"""
日期: 2022-10-24
题目: 分割数组
链接: https://leetcode-cn.com/problems/partition-array-into-disjoint-intervals/
"""

from typing import *
from collections import *
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = [nums[0]]
        right_min = [nums[-1]]
        
        for i in range(1, n - 1):
            left_max.append(max(nums[i], left_max[-1]))
        
        for i in range(n - 2, 0, -1):
            right_min.append(min(nums[i], right_min[-1]))
        
        right_min = right_min[::-1]
        
        for i in range(n - 1):
            if left_max[i] <= right_min[i]:
                return i + 1

test = Solution()
print(test.partitionDisjoint([1, 1, 1, 1]))
        
