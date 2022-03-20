from typing import List
import heapq
import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        for i in range(n):
            piles[i] = -piles[i]
        heapq.heapify(piles)
        for _ in range(k):
            temp = -heapq.heappop(piles)
            rest = temp - math.floor(temp / 2)
            heapq.heappush(piles, -rest)
        return -sum(piles)
test = Solution()
print(test.minStoneSum([4,3,6,7], 3))
