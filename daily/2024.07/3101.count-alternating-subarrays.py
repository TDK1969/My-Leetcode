"""
日期: 2024-07-06
题目: 交替子数组计数
链接: https://leetcode.cn/problems/count-alternating-subarrays/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 1
        pre = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                pre += 1
            else:
                pre = 1
            ans += pre
                
        
        return ans

print(Solution().countAlternatingSubarrays([1,0,1,0]))

"""
--TESTCASE BEGIN--
TestCase 0: [0,1,1,1]
TestCase 1: [1,0,1,0]
--TESTCASE END--
""" 
