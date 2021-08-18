class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(7)] for _ in range(n)]
        # 0-A结尾，1-P结尾，前面不含A，2-P结尾，前面含A，3-L结尾，前面不含A
        # 4-单L结尾，前面含A，5-LL结尾，前面不含A，6-LL结尾，前面含A
        dp[0][0] = 1
        dp[0][1] = 1
        dp[0][3] = 1

        for i in range(1, n):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5]) % mod
            dp[i][1] = (dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5]) % mod
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][4] + dp[i - 1][6]) % mod
            dp[i][3] = (dp[i - 1][1]) % mod
            dp[i][4] = (dp[i - 1][0] + dp[i - 1][2]) % mod
            dp[i][5] = (dp[i - 1][3]) % mod
            dp[i][6] = (dp[i - 1][4]) % mod

        return sum(dp[-1]) % mod

test = Solution()
print(test.checkRecord(10101))

