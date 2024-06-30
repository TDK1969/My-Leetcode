"""
日期: 2024-04-19
题目: 准时抵达会议现场的最小跳过休息次数
链接: https://leetcode.cn/problems/minimum-skips-to-arrive-at-meeting-on-time/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [1,3,2],4,2
TestCase 1: [7,3,5,5],2,10
TestCase 2: [7,3,5,5],1,10
--TESTCASE END--
""" 
