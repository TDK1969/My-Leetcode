"""
日期: 2023-09-24
题目: LRU 缓存
链接: https://leetcode-cn.com/problems/lru-cache/
"""

from typing import *
from collections import *
class Node:
    def __init__(self, pre: "Node", nxt: "Node", key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.pre = pre
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.len = 0
        self.head = Node(None, None, -1, -1)
        self.tail = Node(None, None, -1, -1)
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.d = {}


    def get(self, key: int) -> int:
        
        if key in self.d:
            update_node = self.d[key]
            update_node.pre.nxt = update_node.nxt
            update_node.nxt.pre = update_node.pre
            update_node.pre = self.head
            update_node.nxt = self.head.nxt
            self.head.nxt.pre = update_node
            self.head.nxt = update_node
            
            return update_node.value
        
        else:
            
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            update_node = self.d[key]
            update_node.value = value
            update_node.pre.nxt = update_node.nxt
            update_node.nxt.pre = update_node.pre
            update_node.pre = self.head
            update_node.nxt = self.head.nxt
            self.head.nxt.pre = update_node
            self.head.nxt = update_node
            return
        
        if self.len == self.c:
            # 达到最大容量,需要逐出最近未使用
            delete_node = self.tail.pre
            delete_node.pre.nxt = self.tail
            self.tail.pre = delete_node.pre
            self.d.pop(delete_node.key)
            self.len -= 1

        
        # 未达到最大容量,可以直接插入
        new_node = Node(self.head, self.head.nxt, key, value)
        self.d[key] = new_node
        self.head.nxt.pre = new_node
        self.head.nxt = new_node
        self.len += 1

        
    
    def debug(self):
        l = []
        k = self.head.nxt
        while k != self.tail:
            l.append(str(k.key))
            k = k.nxt
        print("->".join(l))

        
test = LRUCache(3)
test.put(1, 1)
test.put(2, 2)
test.put(3, 3)
test.put(4, 4)
print(test.get(4))
print(test.get(3))
print(test.get(2))
print(test.get(1))
test.put(5, 5)
print(test.get(1))
print(test.get(2))
print(test.get(3))
print(test.get(4))
print(test.get(5))      
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)