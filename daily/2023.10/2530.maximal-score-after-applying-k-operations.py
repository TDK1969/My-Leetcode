"""
日期: 2023-10-18
题目: 执行 K 次操作后的最大分数
链接: https://leetcode-cn.com/problems/maximal-score-after-applying-k-operations/
"""

from typing import *
from collections import *
import math
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)
        for num in nums:
            heapq.heappush(h, -num)
        ans = 0
        for _ in range(k):
            t = -heapq.heappop(h)
            #print(f"{t} -> {math.ceil(t / 3)}")
            print(f"{t} -> {(t + 2) // 3}")
            ans += t
            heapq.heappush(h, -((t + 2) // 3))
        return ans

test = Solution()
print(test.maxKelements([238838724,196963851,539418658,120132686,273213807,57187185,68854249,619718192], 7))
