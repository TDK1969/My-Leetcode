from typing import List


class Solution:
    def uniquePathsWith0bstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(col):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

test = Solution()
print(test.uniquePathsWith0bstacles([[0,0,0],[0,1,0],[0,0,0]]))