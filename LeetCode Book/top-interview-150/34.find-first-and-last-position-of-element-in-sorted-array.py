"""
日期: 2024-02-08
题目: 在排序数组中查找元素的第一个和最后一个位置
链接: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = [-1, -1]
        if n == 0:
            return ans
        # 找右边界
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) >> 1 
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if 0 <= r < n and nums[r] == target:
            ans[1] = r
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        if 0 <= l < n and nums[l] == target:
            ans[0] = l
        
        return ans

print(Solution().searchRange([4, 4], 4))
        
        
"""
--TESTCASE BEGIN--
TestCase 0: [5,7,7,8,8,10],8
TestCase 1: [5,7,7,8,8,10],6
TestCase 2: [],0
--TESTCASE END--
""" 
