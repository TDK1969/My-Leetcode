from typing import List

import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        if index >= len(nums) or nums[index] != target:
            return -1
        return index
    def my_search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1