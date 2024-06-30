"""
日期: 2024-06-21
题目: 气温变化趋势
链接: https://leetcode.cn/problems/6CE719/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        n = len(temperatureA)
        ans = 0
        pre = 0
        for i in range(n - 1):
            if temperatureA[i + 1] > temperatureA[i] and temperatureB[i + 1] > temperatureB[i] or \
            temperatureA[i + 1] == temperatureA[i] and temperatureB[i + 1] == temperatureB[i] or \
            temperatureA[i + 1] < temperatureA[i] and temperatureB[i + 1] < temperatureB[i]:
                ans = max(ans, i - pre + 1)
            else:
                pre = i + 1
        return ans

print(Solution().temperatureTrend([5,10,16,-6,15,11,3],[16,22,23,23,25,3,-16]))

"""
--TESTCASE BEGIN--
TestCase 0: [21,18,18,18,31],[34,32,16,16,17]
TestCase 1: [5,10,16,-6,15,11,3],[16,22,23,23,25,3,-16]
--TESTCASE END--
""" 
