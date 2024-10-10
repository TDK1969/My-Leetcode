"""
日期: 2024-07-31
题目: 覆盖所有点的最少矩形数目
链接: https://leetcode.cn/problems/minimum-rectangles-to-cover-points/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]],1
TestCase 1: [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]],2
TestCase 2: [[2,3],[1,2]],0
--TESTCASE END--
""" 
