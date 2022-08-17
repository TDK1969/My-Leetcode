"""
日期: 2022-08-16
题目: 设计有序流
链接: https://leetcode-cn.com/problems/design-an-ordered-stream/
"""

from typing import *
from collections import *
class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 0
        self.stream = ["" for _ in range(n)]



    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        i = self.ptr
        while i < self.n and self.stream[i]:
            i += 1
        ans = self.stream[self.ptr:i]
        self.ptr = i
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)