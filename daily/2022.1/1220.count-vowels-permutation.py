class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [1, 1, 1, 1, 1]
        mod = 10 ** 9 + 7

        for _ in range(1, n):
            dp[0], dp[1], dp[2], dp[3], dp[4] = \
                (dp[1] + dp[4] + dp[2]) % mod, \
                (dp[0] + dp[2]) % mod, \
                (dp[1] + dp[3]) % mod, \
                (dp[2]) % mod, \
                (dp[2] + dp[3]) % mod

        return sum(dp) % mod

test = Solution()
print(test.countVowelPermutation(5))