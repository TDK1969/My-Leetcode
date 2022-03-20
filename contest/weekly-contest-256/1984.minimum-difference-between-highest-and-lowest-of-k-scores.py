from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float("inf")
        for i in range(len(nums)):
            if i + k - 1 >= len(nums):
                return ans
            ans = min(ans, nums[i + k - 1] - nums[i])
        return ans
test = Solution()
print(test.minimumDifference([-100, 1, 2, 50], 2))