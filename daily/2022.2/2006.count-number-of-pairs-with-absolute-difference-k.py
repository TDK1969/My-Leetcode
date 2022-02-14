from typing import List
from collections import Counter

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        ans = 0
        for i in count:
            if i + k in count:
                ans += count[i] * count[i + k]
        return ans


