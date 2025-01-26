"""
日期: 2025-01-17
题目: 或值至少为 K 的最短子数组 II
链接: https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3],2
TestCase 1: [2,1,8],10
TestCase 2: [1,2],0
--TESTCASE END--
""" 
