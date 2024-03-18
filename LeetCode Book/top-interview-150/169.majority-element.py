"""
日期: 2022-09-14
题目: 多数元素
链接: https://leetcode-cn.com/problems/majority-element/
"""

from typing import *
from collections import *
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = -1
        major_cnt = 0
        other_cnt = 0

        i = 0
        n = len(nums)

        while i < n:
            major = nums[i]
            major_cnt = 1
            other_cnt = 0
            i += 1
            while i < n:
                if nums[i] == major:
                    major_cnt += 1
                else:
                    other_cnt += 1
                i += 1
                if other_cnt >= major_cnt:
                    break
        return major
            
                
