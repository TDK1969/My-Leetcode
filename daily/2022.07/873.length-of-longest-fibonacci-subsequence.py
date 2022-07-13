"""
日期: 2022-07-09
题目: 最长的斐波那契子序列的长度
链接: https://leetcode-cn.com/problems/length-of-longest-fibonacci-subsequence/
"""

from typing import *
from collections import *
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[2 for _ in range(n)] for _ in range(n)]
        # dp[i][j]
        index = {v : i for i, v in enumerate(arr)}

        ans = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] >= 2 * arr[i]:
                    break
                else:
                    if arr[j] - arr[i] in index:
                        dp[i][j] = max(dp[i][j], dp[index[arr[j] - arr[i]]][i] + 1)
                        ans = max(ans, dp[i][j])
        return ans if ans > 2 else 0

test = Solution()
print(test.lenLongestFibSubseq( arr = [1,2,3,4,5,6,7,8]))