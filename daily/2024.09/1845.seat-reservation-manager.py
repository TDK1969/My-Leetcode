"""
日期: 2024-09-30
题目: 座位预约管理系统
链接: https://leetcode.cn/problems/seat-reservation-manager/
"""

from typing import *
from collections import *
from leetcode_utils import *
import heapq
class SeatManager:

    def __init__(self, n: int):
        self.seats = []
        heapq.heapify(self.seats)
        for i in range(1, n + 1):
            heapq.heappush(self.seats, i)

    def reserve(self) -> int:
        return heapq.heappop(self.seats)
    
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

"""
--TESTCASE BEGIN--
TestCase 0: ["SeatManager","reserve","reserve","unreserve","reserve","reserve","reserve","reserve","unreserve"],[[5],[],[],[2],[],[],[],[],[5]]
--TESTCASE END--
""" 
