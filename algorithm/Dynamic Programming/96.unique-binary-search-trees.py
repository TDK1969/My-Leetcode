class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for l in range(i):
                r = i - l - 1
                dp[i] += dp[r] * dp[l]
        return dp[-1]

test = Solution()
print(test.numTrees(2))
