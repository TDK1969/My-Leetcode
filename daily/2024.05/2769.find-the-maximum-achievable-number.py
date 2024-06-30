"""
日期: 2024-05-21
题目: 找出最大的可达成数字
链接: https://leetcode.cn/problems/find-the-maximum-achievable-number/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t

"""
--TESTCASE BEGIN--
TestCase 0: 4,1
TestCase 1: 3,2
--TESTCASE END--
""" 
