"""
日期: 2024-09-01
题目: 在既定时间做作业的学生人数
链接: https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3],[3,2,7],4
TestCase 1: [4],[4],4
--TESTCASE END--
""" 
