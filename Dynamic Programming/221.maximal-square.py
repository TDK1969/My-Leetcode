from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maxline = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    maxline = 1

        if maxline == 0:
            return 0

        for length in range(2, min(m, n) + 1):
            temp1 = []
            for i in range(m - length + 1):
                temp2 = []
                for j in range(n - length + 1):
                    check = dp[i][j] & dp[i][j + 1] & dp[i + 1][j] & dp[i + 1][j + 1]
                    if check:
                        maxline = max(maxline, length)
                    temp2.append(check)
                temp1.append(temp2)
            dp = temp1

        return maxline ** 2

test = Solution()
print(test.maximalSquare([["1","1"],["1","1"]]))



