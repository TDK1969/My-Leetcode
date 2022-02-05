from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxGold = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(x: int, y: int, gold: int):
            if grid[x][y] != 0:
                curGold = gold + grid[x][y]
                nonlocal maxGold
                maxGold = max(maxGold, curGold)
                temp = grid[x][y]
                grid[x][y] = 0

                for dx, dy in dir:
                    nxtX, nxtY = x + dx, y + dy
                    if 0 <= nxtX < m and 0 <= nxtY < n and grid[nxtX][nxtY] != 0:
                        dfs(nxtX, nxtY, curGold)

                grid[x][y] = temp



        for i in range(m):
            for j in range(n):
                dfs(i, j, 0)

        return maxGold

test = Solution()
print(test.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))




