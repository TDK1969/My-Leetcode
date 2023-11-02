from typing import *
from collections import *


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        directions = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
        x, y, index = 0, 0, 0
        n = len(grid)
        while index < n * n - 1:
            flag = False
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == index + 1:
                    flag = True
                    index += 1
                    x, y = nx, ny
                    break
            if not flag:
                return False
        return True

test = Solution()
print(test.checkValidGrid([[8,3,6],[5,0,1],[2,7,4]]))

        