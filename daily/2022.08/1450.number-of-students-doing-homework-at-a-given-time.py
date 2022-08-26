"""
日期: 2022-08-19
题目: 在既定时间做作业的学生人数
链接: https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time/
"""

from typing import *
from collections import *
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                ans += 1
        return ans