from typing import List
from collections import defaultdict
import bisect


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        count = {}

        for i, num in enumerate(nums):
            if num not in count:
                count[num] = i
            else:
                if i - count[num] <= k:
                    return True
                count[num] = i
        return False

test = Solution()
print(test.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))

                


