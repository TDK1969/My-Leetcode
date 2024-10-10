"""
日期: 2024-07-10
题目: 统计移除递增子数组的数目 I
链接: https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        def check(nums: List[int]):
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:
                    return False
            return True
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if check(nums[:i] + nums[j:]):
                    print(nums[i:j])
                    ans += 1
        return ans

print(Solution().incremovableSubarrayCount([6,5,7,8]))
"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,4]
TestCase 1: [6,5,7,8]
TestCase 2: [8,7,6,6]
--TESTCASE END--
""" 
