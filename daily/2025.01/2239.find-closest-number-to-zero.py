"""
日期: 2025-01-20
题目: 找到最接近 0 的数字
链接: https://leetcode.cn/problems/find-closest-number-to-zero/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = 10**5 + 1
        for num in nums:
            if abs(num) < abs(ans) or abs(num) == abs(ans) and num > ans:
                ans = num
        return ans

"""
--TESTCASE BEGIN--
TestCase 0: [-4,-2,1,4,8]
TestCase 1: [2,-1,1]
--TESTCASE END--
""" 
