"""
日期: 2024-09-18
题目: 坐上公交的最晚时间
链接: https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [10,20],[2,17,18,19],2
TestCase 1: [20,30,10],[19,13,26,4,25,11,21],2
--TESTCASE END--
""" 
