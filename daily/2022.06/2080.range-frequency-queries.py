"""
日期: 2022-06-07
题目: 爱吃香蕉的珂珂
链接: https://leetcode-cn.com/problems/koko-eating-bananas/
"""
from typing import *
from collections import *
class Node:
    def __init__(self, l: int = -1, r: int = -1) -> None:
        self.l = l
        self.r = r
        self.c = Counter()

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.trees = defaultdict(Node)
        
        def build(l: int, r: int, idx: int):
            self.trees[idx].l = l
            self.trees[idx].r = r
            if l == r:
                self.trees[idx].c[arr[l]] = 1
            else:
                mid = (l + r) >> 1
                build(l, mid, idx * 2)
                build(mid + 1, r, idx * 2 + 1)
                self.trees[idx].c += self.trees[idx * 2].c + self.trees[idx * 2 + 1].c
        
        build(0, len(arr) - 1, 1)          

    def query(self, left: int, right: int, value: int) -> int:
        
        def q(idx: int) -> int:
            if left > self.trees[idx].r or right < self.trees[idx].l:
                return 0
            if left <= self.trees[idx].l and self.trees[idx].r <= right:
                return self.trees[idx].c[value]
            else:
                return q(idx * 2) + q(idx * 2 + 1)
            
        return q(1)


test = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
print(test.query(0, 11, 33))


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)