from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        ans = len(nums) - nums.count(max(nums)) - nums.count(min(nums))
        return ans if ans > 0 else 0
