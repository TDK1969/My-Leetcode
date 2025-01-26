"""
日期: 2024-11-08
题目: 判断矩形的两个角落是否可达
链接: https://leetcode.cn/problems/check-if-the-rectangle-corner-is-reachable/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        

"""
--TESTCASE BEGIN--
TestCase 0: 3,4,[[2,1,1]]
TestCase 1: 3,3,[[1,1,2]]
TestCase 2: 3,3,[[2,1,1],[1,2,1]]
TestCase 3: 4,4,[[5,5,1]]
--TESTCASE END--
""" 
