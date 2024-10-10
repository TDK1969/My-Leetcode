"""
日期: 2024-07-23
题目: 求出所有子序列的能量和
链接: https://leetcode.cn/problems/find-the-sum-of-subsequence-powers/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,4],3
TestCase 1: [2,2],2
TestCase 2: [4,3,-1],2
--TESTCASE END--
""" 
