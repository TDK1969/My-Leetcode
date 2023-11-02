import bisect
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        n = len(nums)
        if 0 <= l < n and 0 <= r <= n and nums[l] == nums[r - 1] == target:
            return [l, r - 1]
        else:
            return [-1, -1]

print(Solution().searchRange([3, 5, 5, 8, 8, 8, 10], 8))