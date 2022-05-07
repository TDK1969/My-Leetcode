"""
日期: 2022-05-08
题目: 数组中重复的数据
链接: https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/
"""

from typing import *
from collections import *
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            i = abs(num)
            if nums[i - 1] < 0:
                ans.append(i)
            else:
                nums[i - 1] *= -1
        return ans