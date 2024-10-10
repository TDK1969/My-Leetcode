import heapq
from typing import List
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = []
        n = len(nums)
        heapq.heapify(h)

        for index, value in enumerate(nums):
            heapq.heappush(h, (value, index))
        
        for _ in range(k):
            v, i = heapq.heappop(h)
            heapq.heappush(h, (v * multiplier, i))
        
        ans = [-1 for _ in range(n)]
        while h:
            v, i = heapq.heappop(h)
            ans[i] = v

        return ans

print(Solution().getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))