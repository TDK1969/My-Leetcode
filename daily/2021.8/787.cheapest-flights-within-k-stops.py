from typing import List
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float("inf") for _ in range(n)]
        dp[src] = 0
        for i in range(k + 1):
            tmp = dp[:]
            for s, d, cost in flights:
                dp[d] = min(dp[d], tmp[s] + cost)
        return dp[dst] if dp[dst] != float("inf") else -1

test = Solution()
print(test.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))





