"""
日期: 2023-02-05
题目: 穿过迷宫的最少移动次数
链接: https://leetcode-cn.com/problems/minimum-moves-to-reach-target-with-rotations/
"""

from typing import *
from collections import *
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[[0, 0] for _ in range(n)] for _ in range(n)]
        q = deque()

        # 0 - 水平, 1 - 垂直
        # (x, y, 姿态, 步数)
        q.append((0, 0, 0, 0))
        visited[0][0][0] = 1
        ans = -1

        while q:
            x, y, pos, step = q.popleft()
            # 到达终点
            if x == n - 1 and y == n - 2 and pos == 0:
                ans = step
                break
            
            # move right
            
            if pos == 0 and y <= n - 3 and visited[x][y + 1][pos] == 0 and grid[x][y + 2] == 0:
                q.append((x, y + 1, pos, step + 1))
                visited[x][y + 1][pos] = 1
            elif pos == 1 and x <= n - 2 and y <= n - 2 and visited[x][y + 1][pos] == 0 and grid[x][y + 1] == grid[x + 1][y + 1] == 0:
                q.append((x, y + 1, pos, step + 1))
                visited[x][y + 1][pos] = 1
            # move down
            
            if pos == 0 and x <= n - 2 and y <= n - 2 and visited[x + 1][y][pos] == 0 and grid[x + 1][y] == grid[x + 1][y + 1] == 0:
                q.append((x + 1, y, pos, step + 1))
                visited[x + 1][y][pos] = 1
            elif pos == 1 and x <= n - 3 and visited[x + 1][y][pos] == 0 and  grid[x + 2][y] == 0:
                q.append((x + 1, y, pos, step + 1))
                visited[x + 1][y][pos] = 1
            # spin
            if visited[x][y][1 - pos] == 0 and x <= n - 2 and y <= n - 2 and\
                 grid[x][y + 1] == grid[x + 1][y] == grid[x + 1][y + 1] == 0:
                q.append((x, y, 1 - pos, step + 1))
                visited[x][y][1 - pos] = 1

        return ans
            
test = Solution()
print(test.minimumMoves(grid = [[0,0,0,0,0,1],   [1,1,0,0,1,0],              [0,0,0,0,1,1],             [0,0,1,0,1,0],           [0,1,1,0,0,0],              [0,1,1,0,0,0]]))