"""
日期: 2024-05-25
题目: 找出满足差值条件的下标 I
链接: https://leetcode.cn/problems/find-indices-with-index-and-value-difference-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = [-1, -1]
        n = len(nums)
        for i in range(n):
            for j in range(i - indexDifference + 1):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    ans[0], ans[1] = i, j
        return ans
"""
--TESTCASE BEGIN--
TestCase 0: [5,1,4,1],2,4
TestCase 1: [2,1],0,0
TestCase 2: [1,2,3],2,4
--TESTCASE END--
""" 
