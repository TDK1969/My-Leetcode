"""
日期: 2024-09-23
题目: 最佳观光组合
链接: https://leetcode.cn/problems/best-sightseeing-pair/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        pre_max_i = values[0]
        for i in range(1, len(values)):
            ans = max(ans, pre_max_i + values[i] - i)
            pre_max_i = max(pre_max_i, values[i] + i)
        return ans

print(Solution().maxScoreSightseeingPair([8,1,5,2,6]))
"""
--TESTCASE BEGIN--
TestCase 0: [8,1,5,2,6]
TestCase 1: [1,2]
--TESTCASE END--
""" 
