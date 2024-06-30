"""
日期: 2024-06-11
题目: 甲板上的战舰
链接: https://leetcode.cn/problems/battleships-in-a-board/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        visited = set()
        m, n = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X" and (i, j) not in visited:
                    visited.add((i, j))
                    q = deque()
                    q.append((i, j))

                    while q:
                        x, y = q.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "X" and(nx, ny) not in visited:
                                visited.add((nx, ny))
                                q.append((nx, ny))
                    
                    ans += 1
        
        return ans

print(Solution().countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))



            

"""
--TESTCASE BEGIN--
TestCase 0: [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
TestCase 1: [["."]]
--TESTCASE END--
""" 
