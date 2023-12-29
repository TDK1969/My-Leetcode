"""
日期: 2023-12-24
题目: 被围绕的区域
链接: https://leetcode-cn.com/problems/surrounded-regions/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        visited = set()
        m, n = len(board), len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    visited.add((i, j))
                    q = deque()
                    q.append((i, j))
                    flag = False
                    area = [(i, j)]

                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        flag = True

                    while q:
                        x, y = q.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "O" and (nx, ny) not in visited:
                                visited.add((nx, ny))
                                area.append((nx, ny))
                                q.append((nx, ny))

                                if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                                    flag = True
                    
                    if not flag:
                        for x, y in area:
                            board[x][y] = "X"

                    



"""
--TESTCASE BEGIN--
TestCase 0: [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
TestCase 1: [["X"]]
--TESTCASE END--
""" 
