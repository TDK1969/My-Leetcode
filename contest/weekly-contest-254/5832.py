from typing import List
import heapq

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        big = []
        small = []
        heapq.heapify(small)
        heapq.heapify(big)
        for num in nums:
            heapq.heappush(big, -num)
            heapq.heappush(small, num)
        while len(ans) < len(nums):
            ans.append(-heapq.heappop(big))
            ans.append(heapq.heappop(small))
        if len(ans) > len(nums):
            ans.pop()
        return ans
test = Solution()
print(test.rearrangeArray([1,2,5,9]))
