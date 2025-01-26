"""
日期: 2024-11-13
题目: 统计满足 K 约束的子字符串数量 II
链接: https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        

"""
--TESTCASE BEGIN--
TestCase 0: "0001111",2,[[0,6]]
TestCase 1: "010101",1,[[0,5],[1,4],[2,3]]
--TESTCASE END--
""" 
