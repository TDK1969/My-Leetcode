"""
日期: 2023-12-26
题目: 参加考试的最大学生数
链接: https://leetcode-cn.com/problems/maximum-students-taking-exam/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        self.ans = 0
        self.cnt = 0
        m, n = len(seats), len(seats[0])
        directions = [[-1, -1], [-1, 1], [0, -1], [0, 1]]
        valid_seats = []
        for i in range(m):
            for j in range(n):
                if seats[i][j] == ".":
                    valid_seats.append((i, j))

        def dfs(idx: int):
            if idx == len(valid_seats):
                self.ans = max(self.ans, self.cnt)
                return
            flag = True
            for dx, dy in directions:
                nx, ny = valid_seats[idx][0] + dx, valid_seats[idx][1] + dy
                if 0 <= nx < m and 0 <= ny < n and seats[nx][ny] == "$":
                    flag = False
            if flag:
                # 该位置选用
                seats[valid_seats[idx][0]][valid_seats[idx][1]] = "$"
                self.cnt += 1
                dfs(idx + 1)
                seats[valid_seats[idx][0]][valid_seats[idx][1]] = "."
                self.cnt -= 1
            # 该位置不选用
            dfs(idx + 1)
    
        dfs(0)
        return self.ans
"""
--TESTCASE BEGIN--
TestCase 0: [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]
TestCase 1: [[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]
TestCase 2: [["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]]
--TESTCASE END--
""" 
print(Solution().maxStudents([["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]]))