"""
日期: 2024-04-11
题目: 互质树
链接: https://leetcode.cn/problems/tree-of-coprimes/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:

"""
--TESTCASE BEGIN--
TestCase 0: [2,3,3,2],[[0,1],[1,2],[1,3]]
TestCase 1: [5,6,10,2,3,6,15],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
--TESTCASE END--
""" 
