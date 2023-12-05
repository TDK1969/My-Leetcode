"""
日期: 2023-11-18
题目: 数位和相等数对的最大和
链接: https://leetcode-cn.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
"""

from typing import *
from collections import *
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_max = dict()
        ans = -1
        for num in nums:
            digit_sum = 0
            temp = num
            while temp:
                digit_sum += temp % 10
                temp //= 10
            if digit_sum not in digit_sum_max:
                digit_sum_max[digit_sum] = [-float("inf"), -float("inf")]
            
            if num >= digit_sum_max[digit_sum][0]:
                digit_sum_max[digit_sum] = [num, digit_sum_max[digit_sum][0]]
            elif num >= digit_sum_max[digit_sum][1]:
                digit_sum_max[digit_sum][1] = num
            
            ans = max(ans, sum(digit_sum_max[digit_sum]))
        
        return ans




"""
--TESTCASE BEGIN--
TestCase 0: [18,43,36,13,7]
TestCase 1: [10,12,19,14]
--TESTCASE END--
""" 

print(Solution().maximumSum([10,12,19,14]))