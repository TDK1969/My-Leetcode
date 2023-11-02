"""
日期: 2023-10-25
题目: 删除有序数组中的重复项 II
链接: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
"""

from typing import *
from collections import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = -1
        right = cnt = 0
        n = len(nums)
        
        while right < n:
            if left != -1 and nums[right] != nums[left]:
                cnt = 0
            if cnt < 2:
                left += 1
                nums[left] = nums[right]
                cnt += 1
            right += 1
        
        return left + 1
test = Solution()
print(test.removeDuplicates([0,0,1,1,1,1,2,3,3]))