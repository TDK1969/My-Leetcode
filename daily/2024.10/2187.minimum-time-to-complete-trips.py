"""
日期: 2024-10-05
题目: 完成旅途的最少时间
链接: https://leetcode.cn/problems/minimum-time-to-complete-trips/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # 二分法
        def check(t: int) -> bool:
            # 检查在t时间内，所有公交车能否完成totalTrips次旅程
            res = 0
            for bus_time in time:
                res += t // bus_time
            return res >= totalTrips
        
        left = 1
        right = min(time) * totalTrips
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                # 如果mid能够完成，则向左找
                right = mid
            else:
                left = mid + 1
        
        return right

print(Solution().minimumTime([2],1))




"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3],5
TestCase 1: [2],1
--TESTCASE END--
""" 
