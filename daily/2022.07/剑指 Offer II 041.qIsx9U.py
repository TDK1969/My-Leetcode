"""
日期: 2022-07-16
题目: 滑动窗口的平均值
链接: https://leetcode-cn.com/problems/qIsx9U/
"""

from typing import *
from collections import *
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = deque()
        self.size = size
        self.s = 0


    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            self.s -= self.window.popleft()
            
        self.window.append(val)
        self.s += val
        return float(self.s / len(self.window))

test = MovingAverage(3)
print(test.next(1))
print(test.next(10))
print(test.next(3))
print(test.next(5))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)