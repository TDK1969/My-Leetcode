"""
题目: 从数量最多的堆取走礼物
链接: https://leetcode-cn.com/problems/take-gifts-from-the-richest-pile/
"""

from typing import *
from collections import *
import heapq
from math import sqrt, floor
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)

        for gift in gifts:
            heapq.heappush(h, -gift)
        
        while h and k:
            t = -heapq.heappop(h)
            a = floor(sqrt(t))
            if a:
                heapq.heappush(h, -a)
            k -= 1
        return -sum(h)

test = Solution()
print(test.pickGifts(gifts = [1,1,1,1], k = 4))