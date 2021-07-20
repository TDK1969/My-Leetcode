from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_pair = 0
        for i in range(n // 2):
            max_pair = max(max_pair, nums[i] + nums[n - i - 1])

        return max_pair
