"""
日期: 2025-01-23
题目: 收集所有金币可获得的最大积分
链接: https://leetcode.cn/problems/maximum-points-after-collecting-coins-from-all-nodes/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        

"""
--TESTCASE BEGIN--
TestCase 0: [[0,1],[1,2],[2,3]],[10,10,3,3],5
TestCase 1: [[0,1],[0,2]],[8,4,4],0
--TESTCASE END--
""" 
