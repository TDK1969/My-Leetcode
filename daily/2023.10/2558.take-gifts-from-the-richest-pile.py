"""
日期: 2023-10-28
题目: 从数量最多的堆取走礼物
链接: https://leetcode-cn.com/problems/take-gifts-from-the-richest-pile/
"""

from typing import *
from collections import *
import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)

        s = 0
        for gift in gifts:
            s += gift
            heapq.heappush(h, -gift)
        
        for _ in range(k):
            t = -heapq.heappop(h)
            left = math.floor(math.sqrt(t))
            s -= (t - left)
            heapq.heappush(h, -left)

            if s == 0:
                break
        
        return s
print(Solution().pickGifts(gifts = [25,64,9,4,100], k = 4))