"""
日期: 2022-07-14
题目: 颜色分类
链接: https://leetcode-cn.com/problems/sort-colors/
"""

from typing import *
from collections import *
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        j = n - 1
        k = 0

        while k < n:
            if nums[k] == 0 and k > i:
                nums[k] = nums[i]
                nums[i] = 0
                i += 1
            elif nums[k] == 2 and k < j:
                nums[k] = nums[j]
                nums[j] = 2
                j -= 1
            else:
                k += 1
test = Solution()
print(test.sortColors([1,1,1,1,1,0,0,0]))

