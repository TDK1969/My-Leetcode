"""
日期: 2024-08-03
题目: 正方形中的最多点数
链接: https://leetcode.cn/problems/maximum-points-inside-the-square/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]],"abdca"
TestCase 1: [[1,1],[-2,-2],[-2,2]],"abb"
TestCase 2: [[1,1],[-1,-1],[2,-2]],"ccd"
--TESTCASE END--
""" 
