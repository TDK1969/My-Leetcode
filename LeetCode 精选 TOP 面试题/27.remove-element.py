"""
日期: 2023-10-25
题目: 移除元素
链接: https://leetcode-cn.com/problems/remove-element/
"""

from typing import *
from collections import *
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        n = len(nums)
        p = 0
        for i in range(n):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
                ans += 1
        nums.reverse()
        return ans
    
test = Solution()
print(test.removeElement(nums = [3,2,2,3], val = 3))
