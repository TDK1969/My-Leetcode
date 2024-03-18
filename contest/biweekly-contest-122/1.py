from typing import *
import heapq
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        h = nums[1:]
        heapq.heapify(h)
        return nums[0] + sum(heapq.nsmallest(2, h))
