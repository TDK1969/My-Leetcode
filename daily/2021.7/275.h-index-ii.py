from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = n = len(citations)

        while l < r:
            mid = (l + r) // 2
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid

        return n - l

test = Solution()
print(test.hIndex([0,1,3,4,5,6]))
