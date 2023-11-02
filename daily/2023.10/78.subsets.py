from typing import *
from collections import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1 << n):
            temp = []
            for j in range(10):
                if i & (1 << j):
                    temp.append(nums[j])
            ans.append(temp)
        return ans

test = Solution()
print(test.subsets([1,2,3]))