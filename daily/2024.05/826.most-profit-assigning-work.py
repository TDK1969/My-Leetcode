"""
日期: 2024-05-17
题目: 安排工作以达到最大收益
链接: https://leetcode.cn/problems/most-profit-assigning-work/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job = list(zip(profit, difficulty))
        job.sort(reverse=True)
        worker.sort(reverse=True)

        i = 0
        p = 0
        for w in worker:
            while i < len(job) and w < job[i][1]:
                i += 1
            if i == len(job):
                break
            p += job[i][0]
        return p

print(Solution().maxProfitAssignment([2,4,6,8,10],[10,20,30,40,50],[4,5,6,7]))

"""
--TESTCASE BEGIN--
TestCase 0: [2,4,6,8,10],[10,20,30,40,50],[4,5,6,7]
TestCase 1: [85,47,57],[24,66,99],[40,25,25]
--TESTCASE END--
""" 
