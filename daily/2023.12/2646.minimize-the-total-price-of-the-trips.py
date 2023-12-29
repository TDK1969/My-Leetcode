"""
日期: 2023-12-06
题目: 最小化旅行的价格总和
链接: https://leetcode-cn.com/problems/minimize-the-total-price-of-the-trips/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: 4,[[0,1],[1,2],[1,3]],[2,2,10,6],[[0,3],[2,1],[2,3]]
TestCase 1: 2,[[0,1]],[2,2],[[0,0]]
--TESTCASE END--
""" 
