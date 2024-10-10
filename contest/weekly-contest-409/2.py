from typing import List
from collections import deque, defaultdict

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        paths = defaultdict(list)
        for i in range(n - 1):
            paths[i].append(i + 1)
        
        ans = []
        for start, end in queries:
            paths[start].append(end)

            q = deque()
            visited = set()
            q.append((0, 0))
            visited.add(0)

            while q:
                cnt, step = q.popleft()
                # 边界条件
                if cnt == n - 1:
                    ans.append(step)
                    break

                for nxt in paths[cnt]:
                    if nxt not in visited:
                        q.append((nxt, step + 1))
                        visited.add(nxt)
            
        return ans

print(Solution().shortestDistanceAfterQueries(  n = 4, queries = [[0, 3], [0, 2]]))
