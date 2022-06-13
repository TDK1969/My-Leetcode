"""
日期: 2022-06-09
题目: 非重叠矩形中的随机点
链接: https://leetcode-cn.com/problems/random-point-in-non-overlapping-rectangles/
"""

from typing import *
from collections import *
import bisect
import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.sums = []
        s = 0
        for a, b ,x, y in rects:
            s += (x - a + 1) * (y - b + 1)
            self.sums.append(s)
        self.s = self.sums[-1]

    def pick(self) -> List[int]:
        r = random.randint(0, self.s)
        i = bisect.bisect_left(self.sums, r)
        x = random.randint(self.rects[i][0], self.rects[i][2])
        y = random.randint(self.rects[i][1], self.rects[i][3])
        return [x, y]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()