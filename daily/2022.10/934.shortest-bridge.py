"""
日期: 2022-10-25
题目: 最短的桥
链接: https://leetcode-cn.com/problems/shortest-bridge/
"""

from typing import *
from collections import *
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        stack = []
        n = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        
                        
        flag = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and flag is False:
                    grid[i][j] = 2
                    stack.append([i, j])
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                                grid[nx][ny] = 2
                                stack.append([nx, ny])
                    flag = True
                if grid[i][j] == 1 and flag is True:
                    visited = set()
                    visited.add((i, j))
                    queue.append([i, j, 0])

                    while queue:
                        x, y, cnt = queue.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:


                
        
        

                    

