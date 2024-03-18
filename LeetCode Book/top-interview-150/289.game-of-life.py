"""
日期: 2023-11-01
题目: 生命游戏
链接: https://leetcode-cn.com/problems/game-of-life/
"""

from typing import *
from collections import *
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for x in range(m):
            for y in range(n):
                cnt = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] & 1:
                        cnt += 1
                if (2 <= cnt <= 3 and board[x][y] & 1) or (cnt == 3 and not board[x][y] & 1):
                    board[x][y] |= 2
        
        for x in range(m):
            for y in range(n):
                board[x][y] = board[x][y] >> 1
        
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(board)
print(board)



