"""
日期: 2024-07-18
题目: 访问消失节点的最少时间
链接: https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:

"""
--TESTCASE BEGIN--
TestCase 0: 3,[[0,1,2],[1,2,1],[0,2,4]],[1,1,5]
TestCase 1: 3,[[0,1,2],[1,2,1],[0,2,4]],[1,3,5]
TestCase 2: 2,[[0,1,1]],[1,1]
--TESTCASE END--
""" 
