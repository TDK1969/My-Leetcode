"""
日期: 2024-08-25
题目: 划分为k个相等的子集
链接: https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

"""
--TESTCASE BEGIN--
TestCase 0: [4,3,2,3,5,2,1],4
TestCase 1: [1,2,3,4],3
--TESTCASE END--
""" 
