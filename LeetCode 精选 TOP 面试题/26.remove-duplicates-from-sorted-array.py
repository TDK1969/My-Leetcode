"""
日期: 2022-07-14
题目: 删除有序数组中的重复项
链接: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import *
from collections import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        n = len(nums)
        while j < n:
            while j < n and nums[i] == nums[j]:
                j += 1
            if j < n:
                i += 1
                nums[i] = nums[j]
                
        return i + 1

test = Solution()
print(test.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))