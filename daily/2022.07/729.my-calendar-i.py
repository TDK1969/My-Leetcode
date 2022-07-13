"""
日期: 2022-07-05
题目: 我的日程安排表 I
链接: https://leetcode-cn.com/problems/my-calendar-i/
"""

from typing import *
from collections import *
class MyCalendar:

    def __init__(self):
        # tree记录某个线段是否被完全预定
        self.tree = set()
        # lazy记录某个线段是否存在预定
        self.lazy = set()

    def book(self, start: int, end: int) -> bool:
        end -= 1

        def query(left: int, right: int, idx: int) -> bool:
            if left > end or right < start:
                return False
            if idx in self.tree:
                return True
            if start <= left and right <= end:
                return idx in self.lazy
            
            mid = (left + right) >> 1
            t1 = query(left, mid, idx << 1)
            t2 = query(mid + 1, right, (idx << 1) + 1)
            return t1 or t2
                
        
        def update(left: int, right: int, idx: int):
            if left > end or right < start:
                return
            if start <= left and right <= end:
                self.tree.add(idx)
                self.lazy.add(idx)
            else:
                mid = (left + right) >> 1
                l_tree = idx << 1
                r_tree = l_tree + 1
                update(left, mid, l_tree)
                update(mid + 1, right, r_tree)
                if l_tree in self.tree and r_tree in self.tree:
                    self.tree.add(idx)
                
                self.lazy.add(idx)

        if not query(0, 10 ** 9, 1):
            update(0, 10 ** 9, 1)
            return True
        else:
            return False

test = MyCalendar()
print(test.book(10, 20))
print(test.book(15, 25))
print(test.book(20, 30))

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)