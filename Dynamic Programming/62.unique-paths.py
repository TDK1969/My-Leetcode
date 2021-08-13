from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        queue = deque()
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

test = Solution()
print(test.uniquePaths(3, 7))

