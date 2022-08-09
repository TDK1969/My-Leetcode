"""
题目: 检查数组是否存在有效划分
链接: https://leetcode-cn.com/problems/check-if-there-is-a-valid-partition-for-the-array/
"""

from typing import *
from collections import *
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n + 1)]
        dp[0] = True

        for i in range(n):
            j = i + 1
            if i >= 1:
                dp[j] = dp[j] or (dp[j - 2] and nums[i] == nums[i - 1])
            if i >= 2:
                dp[j] = dp[j] or (dp[j - 3] and nums[i] == nums[i - 1] == nums[i - 2])
                dp[j] = dp[j] or (dp[j - 3] and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2)
        return dp[-1]

test = Solution()
print(test.validPartition([4,4,4,5,6]))


