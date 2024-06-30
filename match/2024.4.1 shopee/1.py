from typing import List
class Solution:
    def solution(self, costs: List[int], coins: int) :
        # write code here
        n = len(costs)
        dp = [[] for _ in range(coins + 1)]

        for k in range(1, n + 1):
            i = k - 1
            for j in range(coins, costs[i] - 1,  -1):
                if len(dp[j]) < len(dp[j - costs[i]]) + 1:
                    dp[j] = dp[j - costs[i]].copy()
                    dp[j].append(costs[i])
        
        return dp[-1]



print(Solution().solution([10,5,6,11,2,3],10))