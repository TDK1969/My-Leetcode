"""
日期: 2024-10-03
题目: 规定时间内到达终点的最小花费
链接: https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: 30,[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]],[5,1,2,20,20,3]
TestCase 1: 29,[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]],[5,1,2,20,20,3]
TestCase 2: 25,[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]],[5,1,2,20,20,3]
--TESTCASE END--
""" 
