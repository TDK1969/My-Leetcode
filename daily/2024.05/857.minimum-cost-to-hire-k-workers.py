"""
日期: 2024-05-02
题目: 雇佣 K 名工人的最低成本
链接: https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

"""
--TESTCASE BEGIN--
TestCase 0: [10,20,5],[70,50,30],2
TestCase 1: [3,1,10,10,1],[4,8,2,2,7],3
--TESTCASE END--
""" 
