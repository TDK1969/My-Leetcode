class Solution:
    def maxPrice(self, grid) :
        m, n = len(grid), len(grid[0])
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + grid[0][i]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = max(dp[j], dp[j - 1]) + grid[i][j]
        
        return dp[-1]
print(Solution().maxPrice([[1,3,1],[1,5,1],[4,2,1]]))
