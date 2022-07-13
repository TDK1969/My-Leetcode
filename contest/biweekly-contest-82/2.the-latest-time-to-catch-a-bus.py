"""
题目: 坐上公交的最晚时间
链接: https://leetcode-cn.com/problems/the-latest-time-to-catch-a-bus/
"""

from typing import *
from collections import *
import bisect
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        
        j = 0
        n = len(passengers)
        # 模拟乘车
        for bus in buses:   
            c = capacity
            while c and j < n and passengers[j] <= bus:
                c -= 1
                j += 1
        
        j -= 1
        # 模拟结束,此时j为最后一个上车的乘客的下标,c是最后一辆车的剩余量,可根据c判断是否为空车

        t = buses[-1] if c else passengers[j]

        # 从后往前寻找
        while j >= 0 and t == passengers[j]:
            j -= 1
            t -= 1
        
        return t

test = Solution()
print(test.latestTimeCatchTheBus(buses = [10,20], passengers = [2,17,18,19], capacity = 2))


