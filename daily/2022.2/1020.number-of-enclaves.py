from typing import List
from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        visited = set()
        m, n = len(grid), len(grid[0])
        ans = 0

        def bfs(i: int, j: int):
            size = 0
            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            queue = deque()
            flag = False
            queue.append((i, j))
            visited.add((i, j))
            size += 1

            while queue:
                curX, curY = queue.popleft()
                for dx, dy in dir:
                    nxtX, nxtY = curX + dx, curY + dy
                    if 0 <= nxtX < m and 0 <= nxtY < n and grid[nxtX][nxtY] == 1 and (nxtX, nxtY) not in visited:
                        size += 1
                        if nxtX == 0 or nxtX == m - 1 or nxtY == 0 or nxtY == n - 1:
                            flag = True
                        queue.append((nxtX, nxtY))

            if flag:
                nonlocal ans
                ans += size

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)

        return ans


