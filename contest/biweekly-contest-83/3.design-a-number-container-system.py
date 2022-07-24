"""
题目: 设计数字容器系统
链接: https://leetcode-cn.com/problems/design-a-number-container-system/
"""

from typing import *
from collections import *

from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.i = dict()
        self.s = dict()


    def change(self, index: int, number: int) -> None:
        if number not in self.s:
            self.s[number] = SortedList()
        if index not in self.i:
            self.i[index] = number
            self.s[number].add(index)
        elif self.i[index] != number:
            old = self.i[index]
            self.s[old].remove(index)
            self.s[number].add(index)
            self.i[index] = number
        
    def find(self, number: int) -> int:
        if number in self.s and self.s[number]:
            return self.s[number][0]
        else:
            return -1

test = NumberContainers()
print(test.change(2, 10))
print(test.change(2, 10))
print(test.change(3, 10))
print(test.find(10))
print(test.change(2, 10))


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)