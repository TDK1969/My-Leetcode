"""
日期: 2024-01-25
题目: 计算 K 置位下标对应元素的和
链接: https://leetcode.cn/problems/sum-of-values-at-indices-with-k-set-bits/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s = 0
        for i in range(len(nums)):
            if bin(i).count("1") == k:
                s += nums[i]
        return s

print(Solution().sumIndicesWithKSetBits([5,10,1,5,2],1))
"""
--TESTCASE BEGIN--
TestCase 0: [5,10,1,5,2],1
TestCase 1: [4,3,2,1],2
--TESTCASE END--
""" 
