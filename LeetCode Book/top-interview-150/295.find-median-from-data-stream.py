"""
日期: 2024-03-20
题目: 数据流的中位数
链接: https://leetcode-cn.com/problems/find-median-from-data-stream/
"""

from typing import *
from collections import *
from leetcode_utils import *
import heapq
class MedianFinder:

    def __init__(self):
        # 需要保证len(self.left) = len(self.right) 或 len(self.left) = len(self.right) + 1
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if len(self.left) == 0 or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
            if len(self.left) > len(self.right) + 1:
                heapq.heappush(self.right, -heapq.heappop(self.left))
        else:
            heapq.heappush(self.right, num)
            if len(self.right) > len(self.left):
                heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0] * 1.0
        else:
            return (self.right[0] - self.left[0]) / 2


t = MedianFinder()
t.addNum(1)
print(t.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
--TESTCASE BEGIN--
TestCase 0: ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"],[[],[1],[2],[],[3],[]]
--TESTCASE END--
""" 
