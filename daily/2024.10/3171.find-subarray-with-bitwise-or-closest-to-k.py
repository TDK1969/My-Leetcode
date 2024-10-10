"""
日期: 2024-10-09
题目: 找到按位或最接近 K 的子数组
链接: https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,4,5],3
TestCase 1: [1,3,1,3],2
TestCase 2: [1],10
--TESTCASE END--
""" 
