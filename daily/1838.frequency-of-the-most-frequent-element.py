from typing import List
from collections import Counter


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        presums = [0]
        presum = 0
        for num in nums:
            presum += num
            presums.append(presum)

        max_len = 0
        l, r = 0, 0
        while r <= n:
            temp_len = r - l


