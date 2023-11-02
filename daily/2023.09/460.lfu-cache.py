"""
日期: 2023-09-25
题目: LFU 缓存
链接: https://leetcode-cn.com/problems/lfu-cache/
"""

from typing import *
from collections import *

class LFUCache:
    class DoubleListNode:
        class Node:
            def __init__(self, pre: "Node", nxt: "Node", key: int, value: int) -> None:
                self.pre = pre
                self.nxt = nxt
                self.key = key
                self.value = value

    def __init__(self, capacity: int):


    def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)