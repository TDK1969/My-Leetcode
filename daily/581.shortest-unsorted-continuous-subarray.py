from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        ts = sorted(nums)
        n = len(nums)
        s = n
        e = 0
        for i in range(n):
            if nums[i] != ts[i]:
                s = min(s, i)
                e = max(e, i)
        if e > s:
            return e - s + 1
        return 0

test = Solution()
print(test.findUnsortedSubarray([1,3,2,2,2]))
