"""
日期: 2024-01-28
题目: 水壶问题
链接: https://leetcode.cn/problems/water-and-jug-problem/
"""

from typing import *
from collections import *
from leetcode_utils import *
import math
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if jug1Capacity == 0 or jug2Capacity == 0:
            return targetCapacity == 0 or jug1Capacity + jug2Capacity == targetCapacity
        return targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0
"""
--TESTCASE BEGIN--
TestCase 0: 3,5,4
TestCase 1: 2,6,5
TestCase 2: 1,2,3
--TESTCASE END--
""" 
