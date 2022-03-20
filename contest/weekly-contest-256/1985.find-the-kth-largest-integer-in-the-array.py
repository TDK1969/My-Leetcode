from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        t = [int(num) for num in nums]
        t.sort()
        return str(t[-k])