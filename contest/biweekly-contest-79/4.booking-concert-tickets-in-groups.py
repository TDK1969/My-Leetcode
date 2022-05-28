"""
题目: 以组为单位订音乐会的门票
链接: https://leetcode-cn.com/problems/booking-concert-tickets-in-groups/
"""

from typing import *
from collections import *

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.remain_sum = m * n
        self.remain_row = [0 for _ in range(n)]
        #self.pre_row_remain = [m * (i + 1) for i in range(n)]
        self.wrong_per_row = [m * (i + 1) for i in range(n)]
        self.finish_line = 0
        self.record = {}


    def gather(self, k: int, maxRow: int) -> List[int]:
        if k > self.m or k > self.remain_sum or (k, maxRow) in self.record and not self.record[(k, maxRow)] or k > self.wrong_per_row[maxRow]:
            return []

        for i in range(self.finish_line, maxRow + 1):
            if self.m - self.remain_row[i] >= k:
                self.remain_sum -= k
                temp = self.remain_row[i]
                self.remain_row[i] += k    
                return [i, temp]
        self.record[(k, maxRow)] = False
        self.wrong_per_row[maxRow] = min(self.wrong_per_row[maxRow], k)
        return []


    def scatter(self, k: int, maxRow: int) -> bool:
        if k > self.remain_sum or k > self.m * (maxRow + 1) or (k, maxRow) in self.record and not self.record[(k, maxRow)] or k > self.wrong_per_row[maxRow]:
            return False
        temp = k
        backup = self.remain_row.copy()
        t = self.finish_line
        for i in range(t, maxRow + 1):
            if self.remain_row[i] < self.m:
                take = min(temp, self.m - self.remain_row[i])
                temp -= take
                self.remain_row[i] += take
                if self.remain_row == self.m:
                    self.finish_line += 1
                if temp == 0:
                    return True
                
        self.remain_row = backup
        self.record[(k, maxRow)] = False
        self.finish_line = t
        self.wrong_per_row[maxRow] = min(self.wrong_per_row[maxRow], k)
        return False



# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)