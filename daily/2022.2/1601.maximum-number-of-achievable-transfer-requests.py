from typing import List
from collections import Counter

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        def dfs(requests: List[List[int]], index: int, requestsNum: int, degrees: List[int]):
            if index == len(requests):
                for degree in degrees:
                    if degree:
                        return
                nonlocal ans
                ans = max(ans, requestsNum)
                return
            
            dfs(requests, index + 1, requestsNum, degrees)
            degrees[requests[index][0]] -= 1
            degrees[requests[index][1]] += 1
            dfs(requests, index + 1, requestsNum + 1, degrees)
            degrees[requests[index][0]] += 1
            degrees[requests[index][1]] -= 1
        
        degrees = [0 for _ in range(n)]
        dfs(requests, 0, 0, degrees)
        return ans

test = Solution()
print(test.maximumRequests(n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))





