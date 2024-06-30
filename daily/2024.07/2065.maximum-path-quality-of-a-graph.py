"""
日期: 2024-07-01
题目: 最大化一张图中的路径价值
链接: https://leetcode.cn/problems/maximum-path-quality-of-a-graph/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [0,32,10,43],[[0,1,10],[1,2,15],[0,3,10]],49
TestCase 1: [5,10,15,20],[[0,1,10],[1,2,10],[0,3,10]],30
TestCase 2: [1,2,3,4],[[0,1,10],[1,2,11],[2,3,12],[1,3,13]],50
--TESTCASE END--
""" 
