from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = []
        for num in nums:
            p = bisect.bisect_left(l, num)
            if p == len(l):
                l.append(num)
            else:
                l[p] = num
        return len(l)

test = Solution()
print(test.lengthOfLIS([10,9,2,5,3,7,101,18]))
