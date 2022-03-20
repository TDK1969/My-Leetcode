from typing import List


class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp = [0] * 3
        for num in nums:
            dp[num] += dp[num] + (1 if num == 0 else dp[num - 1])
            dp[num] %= 10**9 + 7
        return dp[2]
test = Solution()
print(test.countSpecialSubsequences([0,1,2,2]))