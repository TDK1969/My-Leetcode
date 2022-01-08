from typing import List
from collections import defaultdict

class Solution:
    def number0fArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        d = [dict() for _ in range(n)]
        count = 0

        for i in range(1, n):
            for j in range(i):
                delta = nums[i] - nums[j]
                if delta in d[i]:
                    d[i][delta] += 1
                else:
                    d[i][delta] = 1

                if delta in d[j]:
                    d[i][delta] += d[j][delta]
                    count += d[j][delta]
        return count

test = Solution()
print(test.number0fArithmeticSlices([2,4,6,8,10]))