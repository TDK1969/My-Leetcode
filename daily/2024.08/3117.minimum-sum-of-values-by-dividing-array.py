"""
日期: 2024-08-16
题目: 划分数组得到最小的值之和
链接: https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [1,4,3,3,2],[0,3,3,2]
TestCase 1: [2,3,5,7,7,7,5],[0,7,5]
TestCase 2: [1,2,3,4],[2]
--TESTCASE END--
""" 
