from typing import List

class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.pos = {}
        for i in range(self.m):
            for j in range(self.n):
                self.pos[self.grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        x, y = self.pos[value]
        ans = 0
        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.m and 0 <= ny < self.n:
                ans += self.grid[nx][ny]
        return ans


    def diagonalSum(self, value: int) -> int:
        x, y = self.pos[value]
        ans = 0
        dir = [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.m and 0 <= ny < self.n:
                ans += self.grid[nx][ny]
        return ans


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)