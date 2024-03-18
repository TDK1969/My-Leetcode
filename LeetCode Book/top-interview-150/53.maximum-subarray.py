"""
日期: 2022-07-14
题目: 最大子数组和
链接: https://leetcode-cn.com/problems/maximum-subarray/
"""

from typing import *
from collections import *
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("inf")
        t = 0

        for i in nums:
            t += i
            ans = max(t, ans)
            if t < 0:
                t = 0
        
        return ans

test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
