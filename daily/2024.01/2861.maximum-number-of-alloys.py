"""
日期: 2024-01-27
题目: 最大合金数
链接: https://leetcode.cn/problems/maximum-number-of-alloys/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: 3,2,15,[[1,1,1],[1,1,10]],[0,0,0],[1,2,3]
TestCase 1: 3,2,15,[[1,1,1],[1,1,10]],[0,0,100],[1,2,3]
TestCase 2: 2,3,10,[[2,1],[1,2],[1,1]],[1,1],[5,5]
--TESTCASE END--
""" 
