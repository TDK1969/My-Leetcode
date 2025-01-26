"""
日期: 2024-10-02
题目: 准时到达的列车最小时速
链接: https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/
"""

from typing import *
from collections import *
from leetcode_utils import *
from math import ceil
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # 二分
        if hour <= len(dist) - 1:
            return -1

        def check(speed: int) -> bool:
            res = 0.0
            for i, d in enumerate(dist):
                if i < len(dist) - 1:
                    res += ceil(d / speed)
                else:
                    res += d / speed
            return res <= hour
    
        left = 1
        right = max(dist) * 100

        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        if not check(right):
            return -1
        return right

print(Solution().minSpeedOnTime([1,1,100000],2.01))
"""
--TESTCASE BEGIN--
TestCase 0: [1,3,2],6
TestCase 1: [1,3,2],2.7
TestCase 2: [1,3,2],1.9
--TESTCASE END--
""" 
