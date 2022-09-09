"""
日期: 2022-07-14
题目: 在排序数组中查找元素的第一个和最后一个位置
链接: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

from typing import *
from collections import *
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if not nums:
            return ans
        n = len(nums)
        # 求r,其中r是nums[r] < target的最大下标
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if r + 1 >= n or r + 1 < n and nums[r + 1] != target:
            return ans
        ans[0] = r + 1

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        ans[1] = l - 1
        return ans

test = Solution()
print(test.searchRange([2, 2], 3))


        
            
