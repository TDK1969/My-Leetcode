"""
日期: 2022-06-06
题目: 我的日程安排表 III
链接: https://leetcode-cn.com/problems/my-calendar-iii/
"""

from typing import *
from collections import *
"""
class MyCalendarThree:
    def __init__(self):
        # 使用哈希表表示数,因为本例中数据量为10^9,使用数组模拟可能会发生内存溢出
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, start: int, end: int, l: int, r: int, idx: int):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, idx * 2)
            self.update(start, end, mid + 1, r, idx * 2 + 1)
            self.tree[idx] = self.lazy[idx] + max(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return self.tree[1]
"""
class MyCalendarThree:

    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, start: int, end: int, l: int, r: int, index: int):
        if start > r or end < l:
            return
        elif start <= l and end >= r:
            # 完全覆盖则只更新懒惰标记
            self.lazy[index] += 1
            return
        else:
            # 标记下沉
            mid = (l + r) // 2
            temp_lazy = self.lazy[index]
            self.lazy[index] = 0
            self.lazy[index * 2] += temp_lazy
            self.lazy[index * 2 + 1] += temp_lazy
            
            # 更新子区间
            self.update(start, end, l, mid, index * 2)
            self.update(start, end, mid + 1, r, index * 2 + 1)
            
            # 合并左右子区间,更新index
            self.tree[index] = max(self.tree[index * 2] + self.lazy[index * 2], 
                               self.tree[index * 2 + 1] + self.lazy[index * 2 + 1])

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return self.tree[1] + self.lazy[1]


test  = MyCalendarThree()
print(test.book(10, 20))
print(test.book(50, 60))
print(test.book(10, 40))
print(test.book(5, 15))


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)