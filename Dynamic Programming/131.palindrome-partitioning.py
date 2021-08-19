from typing import List
from collections import deque

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for l in range(n):
                r = l + length - 1
                if r >= n:
                    break
                if s[l] == s[r]:
                    if length == 2:
                        dp[l][r] = True
                    else:
                        dp[l][r] = dp[l + 1][r - 1]
        ans = []
        index = []
        def dfs(i: int):
            if i == n:
                temp = []
                for pair in index:
                    temp.append(s[pair[0]:pair[1] + 1])
                ans.append(temp)
            for j in range(i, n):
                if dp[i][j]:
                    index.append((i, j))
                    dfs(j + 1)
                    index.pop()

        dfs(0)
        return ans

test = Solution()
print(test.partition("aab"))

