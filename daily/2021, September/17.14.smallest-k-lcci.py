from typing import List
import heapq

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        ans = []
        heapq.heapify(arr)
        for i in range(k):
            ans.append(heapq.heappop(arr))
        return ans

