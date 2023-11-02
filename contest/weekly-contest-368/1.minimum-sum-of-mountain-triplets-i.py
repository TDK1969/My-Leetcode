"""
题目: 元素和最小的山形三元组 I
链接: https://leetcode-cn.com/problems/minimum-sum-of-mountain-triplets-i/
"""

from typing import *
from collections import *
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        ans = float("inf")
        pre = nums[0]
        for j in range(1, n - 1):
            if pre < nums[j] > suf[j + 1]:
                ans = min(ans, pre + nums[j] + suf[j + 1])
            pre = min(pre, nums[j])
        return ans if ans < float("inf") else -1

test = Solution()
print(test.minimumSum([8,6,1,5,3]))
        

