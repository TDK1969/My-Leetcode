from typing import *
import heapq
class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        h = [-num for num in nums]
        s = sum(nums)
        heapq.heapify(h)

        while len(h) > 1:
            if s == 0:
                break
            t1, t2 = -heapq.heappop(h), -heapq.heappop(h)
            if t2 == 0:
                
                return len(h) + 2
            k = t2 % t1
            s = s - t1 - t2 + k
            heapq.heappush(h, -k)
        return len(h)

print(Solution().minimumArrayLength([4, 4, 4]))

