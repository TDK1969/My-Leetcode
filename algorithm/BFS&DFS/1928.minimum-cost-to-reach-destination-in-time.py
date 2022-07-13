from typing import List
from collections import defaultdict



class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        lines = defaultdict(list)
        for x, y, time in edges:
            lines[x].append((y, time))
            lines[y].append((x, time))

        dp = [[float("inf") for _ in range(n)] for _ in range(maxTime + 1)]
        dp[0][0] = passingFees[0]
        for i in range(1, maxTime + 1):
            for s, v, time in edges:
                if i >= time:
                    dp[i][s] = min(dp[i][s], dp[i - time][v] + passingFees[s])
                    dp[i][v] = min(dp[i][v], dp[i - time][s] + passingFees[v])
        ans = min(dp[t][-1] for t in range(1, maxTime + 1))
        return -1 if ans == float("inf") else ans


test = Solution()
print(test.minCost(29,[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]],[5,1,2,20,20,3]))



