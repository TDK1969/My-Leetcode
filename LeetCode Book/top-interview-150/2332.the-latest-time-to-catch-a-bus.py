"""
日期: 2024-03-08
题目: 坐上公交的最晚时间
链接: https://leetcode-cn.com/problems/the-latest-time-to-catch-a-bus/
"""

from typing import *
from collections import *
from leetcode_utils import *
import bisect

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        n = len(passengers)
        start = 0
        isFullBus = False
        for bus in buses:
            # passengers[start:i + 1]为能够乘坐bus的乘客
            if start + capacity >= n:
                isFullBus = False
                start = n - 1
                break

            i = bisect.bisect_right(passengers, bus, start, start + capacity)
            isFullBus = (i - start) == capacity
            start = i
        
        start -= 1
        start = max(0, start)
        t = passengers[start] if isFullBus else buses[-1]
        while start >= 0 and t == passengers[start]:
            start -= 1
            t -= 1

        return t    
print(Solution().latestTimeCatchTheBus([2],[2],2))

"""
--TESTCASE BEGIN--
TestCase 0: [10,20],[2,17,18,19],2
TestCase 1: [20,30,10],[19,13,26,4,25,11,21],2
--TESTCASE END--
""" 
