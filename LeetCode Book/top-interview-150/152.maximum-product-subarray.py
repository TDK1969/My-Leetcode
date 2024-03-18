"""
日期: 2024-03-07
题目: 乘积最大子数组
链接: https://leetcode-cn.com/problems/maximum-product-subarray/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -float("inf")
        temp_max = 1
        temp_min = 1
        for num in nums:
            if num > 0:
                temp_max *= num
                temp_min *= num
            else:
                temp_max, temp_min = temp_min * num, temp_max * num
            ans = max(ans, temp_max)
            if temp_max <= 0:
                temp_max = 1
            if temp_min >= 0:
                temp_min = 1
            
        return ans

print(Solution().maxProduct([-4, -3, -2]))
"""
--TESTCASE BEGIN--
TestCase 0: [2,3,-2,4]
TestCase 1: [-2,0,-1]
--TESTCASE END--
""" 
