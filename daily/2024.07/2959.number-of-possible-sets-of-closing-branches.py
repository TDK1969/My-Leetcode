"""
日期: 2024-07-17
题目: 关闭分部的可行集合数目
链接: https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: 3,5,[[0,1,2],[1,2,10],[0,2,10]]
TestCase 1: 3,5,[[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
TestCase 2: 1,10,[]
--TESTCASE END--
""" 
