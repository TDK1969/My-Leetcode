"""
日期: 2022-05-06
题目: 最近的请求次数
链接: https://leetcode-cn.com/problems/number-of-recent-calls/
"""

from typing import *    
from collections import *
import bisect
class RecentCounter:

    def __init__(self):
        self.ping_time = deque()


    def ping(self, t: int) -> int:
        self.ping_time.append(t)
        while self.ping_time[0] < t - 3000:
            self.ping_time.popleft()
        return len(self.ping_time)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)