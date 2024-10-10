"""
日期: 2024-10-08
题目: 旅行终点站
链接: https://leetcode.cn/problems/destination-city/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out = defaultdict(int)
        city = set()
        for s, e in paths:
            out[s] += 1
            city.add(s)
            city.add(e)
        
        for c in city:
            if out[c] == 0:
                return c
        return ""



"""
--TESTCASE BEGIN--
TestCase 0: [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
TestCase 1: [["B","C"],["D","B"],["C","A"]]
TestCase 2: [["A","Z"]]
--TESTCASE END--
""" 
