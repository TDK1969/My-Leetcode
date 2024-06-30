"""
日期: 2024-05-23
题目: 找出最长等值子数组
链接: https://leetcode.cn/problems/find-the-longest-equal-subarray/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        position = defaultdict(list)
        for i, num in enumerate(nums):
            position[num].append(i)
        
        ans = 0
        for p in position.values():
            left = 0
            for right in range(len(p)):
                while p[right] - p[left] - (right - left) > k:
                    left += 1
                ans = max(ans, right - left + 1)

        return ans
print(Solution().longestEqualSubarray([1,3,2,3,1,3],3))
"""
--TESTCASE BEGIN--
TestCase 0: [1,3,2,3,1,3],3
TestCase 1: [1,1,2,2,1,1],2
--TESTCASE END--
""" 
