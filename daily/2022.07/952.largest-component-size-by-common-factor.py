"""
日期: 2022-07-30
题目: 按公因数计算最大组件大小
链接: https://leetcode-cn.com/problems/largest-component-size-by-common-factor/
"""

from typing import *
from collections import *
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        ans = 1
        a = [i for i in range(int(max(nums) ** 0.5) + 2)]
        n = len(nums)

        for i in nums:
            for j in range(1, int(max(nums) ** 0.5) + 1):
                if i % j == 0 and i >= j:
                    



        return ans

test = Solution()
print(test.largestComponentSize(nums = [2,3,6,7,4,12,21,39]))
