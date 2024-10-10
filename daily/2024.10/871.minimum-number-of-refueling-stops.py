"""
日期: 2024-10-07
题目: 最低加油次数
链接: https://leetcode.cn/problems/minimum-number-of-refueling-stops/
"""

from typing import *
from collections import *
from leetcode_utils import *
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        ans = 0
        fuel_heap = []
        heapq.heapify(fuel_heap)

        cur_fuel = startFuel
        cur_pos = 0

        for pos, fuel in stations:
            # 如果到不了，则从fuel_heap中加油
            while pos - cur_pos > cur_fuel:
                if len(fuel_heap) > 0:
                    cur_fuel -= heapq.heappop(fuel_heap)
                    ans += 1
                else:
                    return -1
            
            # 能够到达，将fuel加入优先队列中，更新cur_pos
            cur_fuel -= pos - cur_pos
            cur_pos = pos
            heapq.heappush(fuel_heap, -fuel)
        
        while target - cur_pos > cur_fuel:
            if len(fuel_heap) > 0:
                cur_fuel -= heapq.heappop(fuel_heap)
                ans += 1
            else:
                return -1

        return ans


print(Solution().minRefuelStops(1,1,[]))



"""
--TESTCASE BEGIN--
TestCase 0: 1,1,[]
TestCase 1: 100,1,[[10,100]]
TestCase 2: 100,10,[[10,60],[20,30],[30,30],[60,40]]
--TESTCASE END--
""" 
