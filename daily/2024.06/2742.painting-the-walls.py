"""
日期: 2024-06-28
题目: 给墙壁刷油漆
链接: https://leetcode.cn/problems/painting-the-walls/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # dp[i][j] 表示前i个墙中，有j个墙由付费来刷的最少开销和积累时间
        # dp[i][j] = dp[i - 1][j],dp[i - 1][j - 1] + cost[j]
        n = len(cost)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        cost_sum = time_sum = 0
        for i in range(n):
            cost_sum += cost[i]
            time_sum += time[i]
            dp[i][i][0], dp[i][i][1] = cost_sum, time_sum
        
        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][0], )
            for j in range(1, n - 1):
                # 前i个墙有j个墙是付费，则i-j个免费
                


"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,2],[1,2,3,2]
TestCase 1: [2,3,4,2],[1,1,1,1]
--TESTCASE END--
""" 
