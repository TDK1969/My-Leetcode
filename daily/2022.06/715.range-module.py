"""
日期: 2022-06-20
题目: Range 模块
链接: https://leetcode-cn.com/problems/range-module/
"""

from typing import *
from collections import *
class RangeModule:

    def __init__(self):
        self.trees = defaultdict(bool)


    def addRange(self, left: int, right: int) -> None:
        right -= 1
        def update(l: int, r: int, idx: int) -> None:
            if l > right or r < left:
                return
            elif left <= l <= r <= right:
                print(f"[{l}, {r}] = True")
                self.trees[idx] = True
            else:
                mid = (l + r) >> 1
                update(l, mid, idx << 1)
                update(mid + 1, r, (idx << 1) + 1)
        
        update(1, 20, 1)

    def queryRange(self, left: int, right: int) -> bool:
        right -= 1
        def query(l: int, r: int, idx: int, mask: bool) -> bool:
            if l > right or r < left:
                return True
            elif left <= l <= r <= right:
                print(f"[{l}, {r}] = {self.trees[idx]}")
                return self.trees[idx]
            else:
                mid = (l + r) >> 1
                return query(l, mid, idx << 1) and query(mid + 1, r, (idx << 1) + 1)
        
        return query(1, 20, 1)


    def removeRange(self, left: int, right: int) -> None:
        right -= 1
        def update(l: int, r: int, idx: int, target: bool) -> None:
            if l > right or r < left:
                if target:
                    self.trees[idx] = True
                return
            elif left <= l <= r <= right:
                print(f"[{l}, {r}] = False")
                self.trees[idx] = False
            else:
                if self.trees[idx]:
                    self.trees[idx] = False
                    mid = (l + r) >> 1
                    update(l, mid, idx << 1, True)
                    update(mid + 1, r, (idx << 1) + 1, True)
                else:
                    mid = (l + r) >> 1
                    update(l, mid, idx << 1, False)
                    update(mid + 1, r, (idx << 1) + 1, False)
        
        update(1, 20, 1, self.trees[1])


test = RangeModule()
print(test.addRange(10, 20))
print(test.trees)
print(test.removeRange(14, 16))
print(test.trees)
print(test.queryRange(16, 17))
print(test.trees)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)