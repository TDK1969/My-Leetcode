"""
日期: 2024-05-04
题目: 规划兼职工作
链接: https://leetcode.cn/problems/maximum-profit-in-job-scheduling/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,3],[3,4,5,6],[50,10,40,70]
TestCase 1: [1,2,3,4,6],[3,5,10,6,9],[20,20,100,70,60]
TestCase 2: [1,1,1],[2,3,4],[5,6,4]
--TESTCASE END--
""" 
