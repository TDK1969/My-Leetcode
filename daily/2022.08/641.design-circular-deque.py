"""
日期: 2022-08-15
题目: 设计循环双端队列
链接: https://leetcode-cn.com/problems/design-circular-deque/
"""

from typing import *
from collections import *

class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [0 for _ in range(k)]
        self.front = 0
        self.rear = 0
        self.size = 0
        self.k = k


    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.q[0] = value
            self.front = -1 % self.k
            self.rear = 1
            self.size += 1
            return True
        if not self.isFull():
            self.q[self.front] = value
            self.front = (self.front - 1) % self.k
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.q[0] = value
            self.front = -1 % self.k
            self.rear = 1
            self.size += 1
            return True
        if not self.isFull():
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.k
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.k
            self.size -= 1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.rear = (self.rear - 1) % self.k
            self.size -= 1
            return True

    def getFront(self) -> int:
        return self.q[(self.front + 1) % self.k] if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.q[(self.rear - 1) % self.k] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.k



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()