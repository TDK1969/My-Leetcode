"""
日期: 2022-06-08
题目: 我的日程安排表 II
链接: https://leetcode-cn.com/problems/my-calendar-ii/
"""

from typing import *
from collections import *
class MyCalendarTwo:

    def __init__(self):
        self.trees = defaultdict(int)
        self.lazy = defaultdict(int)
        self.cnt = 0

    def book(self, start: int, end: int) -> bool:

        def query(l: int, r: int, idx: int) -> int:
            if start > r or end < l:
                #print(self.cnt * "\t" + f"[{l}, {r}]: return 0")
                return 0
            if start <= l and r <= end:
                #print(self.cnt * "\t" + f"[{l}, {r}]: return {self.trees[idx]}")
                return self.trees[idx]
            else:
                mid = (l + r) >> 1
                self.cnt += 1
                t1 = query(l, mid, idx * 2)
                t2 = query(mid + 1, r, idx * 2 + 1)
                self.cnt -= 1
                #print(self.cnt * "\t" + f"[{l}, {r}]: return max({t1}, {t2}) + {self.lazy[idx]}")
                return max(t1, t2) + self.lazy[idx]
                
        
        def update(l: int, r: int, idx: int):
            if start > r or end < l:
                return 
            if start <= l and r <= end:
                self.trees[idx] += 1
                self.lazy[idx] += 1
            else:
                mid = (l + r) >> 1
                update(l, mid, idx * 2)
                update(mid + 1, r, idx * 2 + 1)
                self.trees[idx] = self.lazy[idx] + max(self.trees[idx * 2], self.trees[idx * 2 + 1])
            #print(f"[{l}, {r}]: {self.trees[idx]}")
        end -= 1
        if query(0, 40, 1) < 2:
            update(0, 40, 1)
            return True
        return False

test = MyCalendarTwo()
print(test.book(26, 27))    
print(test.book(27, 28))
print(test.book(28, 29))
print(test.book(26, 27))
print(test.book(26, 27))
print(test.book(0, 1))
print(test.book(0, 1))
print(test.book(0, 1))



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)