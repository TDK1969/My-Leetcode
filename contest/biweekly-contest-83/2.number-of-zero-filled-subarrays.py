"""
题目: 全 0 子数组的数目
链接: https://leetcode-cn.com/problems/number-of-zero-filled-subarrays/
"""

from typing import *
from collections import *
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        k = 0
        for num in nums:
            if num == 0:
                k += 1
            else:
                ans += (1 + k) * k // 2
                k = 0
        ans += (1 + k) * k // 2
        return ans

test = Solution()
print(test.zeroFilledSubarray([1, 0, 1, 0, 0]))