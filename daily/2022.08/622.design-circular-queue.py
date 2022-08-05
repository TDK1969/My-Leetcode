"""
日期: 2022-08-02
题目: 设计循环队列
链接: https://leetcode-cn.com/problems/design-circular-queue/
"""

from typing import *
from collections import *
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        self.k = k
        self.queue_len = 0
        self.front = 0
        self.rear = 1


    def enQueue(self, value: int) -> bool:
        if self.queue_len == self.k:
            return False
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.k
            self.queue_len += 1
            return True

    def deQueue(self) -> bool:
        if self.queue_len == 0:
            return False
        else:
            self.queue_len -= 1
            self.front = (self.front + 1) % self.k
            return True

    def Front(self) -> int:
        if self.queue_len == 0:
            return -1
        else:
            return self.queue[self.front]


    def Rear(self) -> int:
        if self.queue_len == 0:
            return -1
        else:
            return self.queue[self.rear - 1]


    def isEmpty(self) -> bool:
        return self.queue_len == 0


    def isFull(self) -> bool:
        return self.queue_len == self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()