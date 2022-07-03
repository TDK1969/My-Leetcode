"""
日期: 2022-06-28
题目: 摆动排序 II
链接: https://leetcode-cn.com/problems/wiggle-sort-ii/
"""

from typing import *
from collections import *
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        half = len(nums[::2])
        nums.sort()
        s = nums[:half]
        s.reverse()
        b = nums[half:]
        b.reverse()
        for i in range(len(s)):
            nums[i * 2] = s[i]
        for j in range(len(b)):
            nums[j * 2 + 1] = b[j]
        print(nums)


test = Solution()
test.wiggleSort([1,1,2,1,2,2,1])
        

        