"""
日期: 2024-09-13
题目: 预算内的最多机器人数目
链接: https://leetcode.cn/problems/maximum-number-of-robots-within-budget/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [3,6,1,3,4],[2,1,3,4,5],25
TestCase 1: [11,12,19],[10,8,7],19
--TESTCASE END--
""" 
