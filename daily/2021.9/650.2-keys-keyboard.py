class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float("inf") for _ in range(n + 1)]
        dp[1] = 0
        for i in range(1, n + 1):
            paste = n // i - 1
            while paste:
                dp[i * (paste + 1)] = min(dp[i * (paste + 1)], dp[i] + paste + 1)
                paste -= 1
        return dp[-1]

test = Solution()
print(test.minSteps(3))