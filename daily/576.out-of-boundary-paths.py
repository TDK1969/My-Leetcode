from collections import deque


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        mod = 10 ** 9 + 7
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # dp[i][j][k] = dp[i-1][j][k-1] + dp[i+1][j][k-1] + dp[i][j-1][k-1] + dp[i][j+1][k-1]
        for k in range(1, maxMove + 1):
            tmp = [[0 for _ in range(n)] for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    for dx, dy in dir:
                        nx = x + dx
                        ny = y + dy
                        if nx < 0 or ny < 0 or nx >= m or ny >= n:
                            # 一步就可出界
                            tmp[x][y] += 1
                        else:
                            tmp[x][y] = (dp[nx][ny] + tmp[x][y]) % mod
            dp = tmp
        return dp[startRow][startColumn]



test = Solution()
print(test.findPaths(2, 2, 2, 0, 0))

