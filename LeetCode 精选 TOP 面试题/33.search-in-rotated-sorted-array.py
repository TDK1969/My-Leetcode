"""
日期: 2022-07-14
题目: 搜索旋转排序数组
链接: https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""

from typing import *
from collections import *
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] < nums[right]:
                # [left, right]为有序区间
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > nums[right]:
                # [left, mid]为有序区间,[mid, right]存在旋转
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                #[left, mid]存在旋转,[mid, right]为有序区间
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
                
            

test = Solution()
print(test.search(nums = [4,5,6,7,8,1,2,3], target = 8))

