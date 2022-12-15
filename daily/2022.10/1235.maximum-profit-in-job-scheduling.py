"""
日期: 2022-10-22
题目: 规划兼职工作
链接: https://leetcode-cn.com/problems/maximum-profit-in-job-scheduling/
"""

from typing import *
from collections import *
import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(endTime, startTime, profit))
        endTime.sort()
        jobs.sort()
        
        n = len(startTime)
        dp = [0] * n
        dp[0] = jobs[0][2]
        for i in range(1, n):
            index = bisect.bisect_right(endTime, jobs[i][1]) - 1
            dp[i] = max(dp[i - 1], dp[index] + jobs[i][2])
        return dp[-1]

