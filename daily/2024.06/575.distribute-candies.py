"""
日期: 2024-06-02
题目: 分糖果
链接: https://leetcode.cn/problems/distribute-candies/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))

"""
--TESTCASE BEGIN--
TestCase 0: [1,1,2,2,3,3]
TestCase 1: [1,1,2,3]
TestCase 2: [6,6,6,6]
--TESTCASE END--
""" 
