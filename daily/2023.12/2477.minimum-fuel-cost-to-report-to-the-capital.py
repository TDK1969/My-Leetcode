"""
日期: 2023-12-05
题目: 到达首都的最少油耗
链接: https://leetcode-cn.com/problems/minimum-fuel-cost-to-report-to-the-capital/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        edges = defaultdict(set)
        for x, y in roads:
            edges[x].add(y)
            edges[y].add(x)
        
        ends = [city for city in edges if len(edges[city]) == 1]
        

"""
--TESTCASE BEGIN--
TestCase 0: [[0,1],[0,2],[0,3]],5
TestCase 1: [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]],2
TestCase 2: [],1
--TESTCASE END--
""" 
