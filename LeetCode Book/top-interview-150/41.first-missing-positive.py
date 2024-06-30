"""
日期: 2022-07-14
题目: 缺失的第一个正数
链接: https://leetcode-cn.com/problems/first-missing-positive/
"""

from typing import *
from collections import *
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            while 0 < nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                t = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = t
            i += 1
        
        j = 1
        while j <= n:
            if nums[j - 1] != j:
                break
            j += 1
        return j

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] != i + 1:
                j = nums[i]
                if j >= n or j < 0 or j < i or nums[j] == j + 1:
                    break


test = Solution()
print(test.firstMissingPositive([2]))

        
