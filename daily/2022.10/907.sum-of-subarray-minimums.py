"""
日期: 2022-10-28
题目: 子数组的最小值之和
链接: https://leetcode-cn.com/problems/sum-of-subarray-minimums/
"""

from typing import *
from collections import *
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = arr[i]
            ans += arr[i]
        
        for i in range(n):
            for j in range(i + 1, n):
                dp[i][j] = min(dp[i][j - 1], arr[j])
                ans = (ans + dp[i][j]) % (10 ** 9 + 7)
        
        return ans

test = Solution()
print(test.sumSubarrayMins([11,81,94,43,3]))

        