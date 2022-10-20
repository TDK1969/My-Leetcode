from typing import *
from collections import *

class ListNode:
    def __init__(self, key: int, value: int, nxt, pre) -> None:
        self.key = key
        self.val = value
        self.nxt = nxt
        self.pre = pre

class LRUCache:
    

    def __init__(self, capacity: int):
        self.head = ListNode(-1, -1, None, None)
        self.tail = ListNode(-1, -1, None, None)
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.d = dict()
        self.len = 0
        self.c = capacity

    def insert(self, key: int, value: int):
        t = ListNode(key, value, None, None)
        self.head.nxt.pre = t
        t.nxt = self.head.nxt
        self.head.nxt = t
        t.pre = self.head
        self.d[key] = t

    def update(self, key: int):
        # 从原位置删除
        node = self.d[key]
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre
        
        # 插入到链表头
        self.head.nxt.pre = node
        node.nxt = self.head.nxt
        self.head.nxt = node
        node.pre = self.head

    def pop_last(self):
        self.d[self.tail.pre.key] = -1
        temp = self.tail.pre
        temp.pre.nxt = temp.nxt
        temp.nxt.pre = temp.pre      
        del temp


    def get(self, key: int) -> int:
        if key in self.d and self.d[key] != -1:
            self.update(key)
            return self.d[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d and self.d[key] != -1:
            self.d[key].val = value
            self.update(key)
        else:
            if self.len == self.c:
                self.pop_last()
                self.len -= 1
            #self.debug()
            self.len += 1
            self.insert(key, value)
    def debug(self):
        t = self.head.nxt
        ans = []
        while t != self.tail:
            ans.append(t.key)
            t = t.nxt
        print(ans)

                
test = LRUCache(3)
test.put(1, 1)
test.put(2, 2)
test.put(3, 3)
test.put(4, 4)
print(test.get(4))
test.debug()
print(test.get(3))
test.debug()
print(test.get(2))
test.debug()
print(test.get(1))
test.debug()
test.put(5, 5)
test.debug()
print(test.get(1))
test.debug()
print(test.get(2))
test.debug()
print(test.get(3))
test.debug()
print(test.get(4))
test.debug()
print(test.get(5))
test.debug()







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)