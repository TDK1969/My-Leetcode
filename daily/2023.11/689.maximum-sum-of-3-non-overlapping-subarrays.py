"""
日期: 2023-11-19
题目: 三个无重叠子数组的最大和
链接: https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,1,2,6,7,5,1],2
TestCase 1: [1,2,1,2,1,2,1,2,1],2
--TESTCASE END--
""" 
