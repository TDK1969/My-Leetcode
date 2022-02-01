from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        height = [[-1 for _ in range(n)] for _ in range(m)]

        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        queue = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    height[i][j] = 0

        while queue:
            x, y = queue.popleft()
            for dx, dy in dir:
                nxtX, nxtY = x + dx, y + dy
                if 0 <= nxtX < m and 0 <= nxtY < n:
                    if height[nxtX][nxtY] == -1:
                        height[nxtX][nxtY] = height[x][y] + 1
                        queue.append((nxtX, nxtY))

        return height

test = Solution()
print(test.highestPeak([[0,0,1],[1,0,0],[0,0,0]]))


