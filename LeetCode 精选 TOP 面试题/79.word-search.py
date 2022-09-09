"""
日期: 2022-07-14
题目: 单词搜索
链接: https://leetcode-cn.com/problems/word-search/
"""

from typing import *
from collections import *
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()
        m = len(board)
        n = len(board[0])
        visited = set()
        
        def search(x: int, y: int, index: int) -> bool:
            if index == len(word):
                return True
            for dx, dy in dirs:
                nxt_x, nxt_y = x + dx, y + dy
                if 0 <= nxt_x < m and 0 <= nxt_y < n and \
                    board[nxt_x][nxt_y] == word[index] and \
                        (nxt_x, nxt_y) not in visited:
                        visited.add((nxt_x, nxt_y))
                        if search(nxt_x, nxt_y, index + 1):
                            return True
                        visited.remove((nxt_x, nxt_y))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if search(i, j, 1):
                        return True
                    visited.remove((i, j))
        
        return False

test = Solution()
print(test.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
