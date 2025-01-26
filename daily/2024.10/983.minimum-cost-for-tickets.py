"""
日期: 2024-10-01
题目: 最低票价
链接: https://leetcode.cn/problems/minimum-cost-for-tickets/
"""

from typing import *
from collections import *
from leetcode_utils import *
import bisect
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float("inf") for _ in range(n + 1)]
        tickets = [[1, costs[0]], [7, costs[1]], [30, costs[2]]]
        dp[0] = 0
        for i in range(1, n + 1):
            for day, cost in tickets:
                l = bisect.bisect_right(days, days[i - 1] - day)
                dp[i] = min(dp[i], dp[l] + cost)
        return dp[-1]

print(Solution().mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))
            
            


"""
--TESTCASE BEGIN--
TestCase 0: [1,4,6,7,8,20],[2,7,15]
TestCase 1: [1,2,3,4,5,6,7,8,9,10,30,31],[2,7,15]
--TESTCASE END--
""" 
