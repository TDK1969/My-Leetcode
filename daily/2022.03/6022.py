from typing import List
import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        heapq.heapify(heapq)

        sumNums = 0
        for num in nums:
            heapq.heappush(heap, -num)
            sumNums += num

        subCount = 0
        k = 0

        while subCount < sumNums / 2:
            temp = -heapq.heappop(heap)
            k += 1
            subCount += temp / 2
            heapq.heappush(heap, -temp / 2)

        return k
