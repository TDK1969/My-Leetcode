"""
日期: 2023-11-01
题目: 两数之和 II - 输入有序数组
链接: https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
"""

from typing import *
from collections import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
        
print(Solution().twoSum(numbers = [2,7,11,15], target = 9))