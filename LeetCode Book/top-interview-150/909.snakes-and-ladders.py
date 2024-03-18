"""
日期: 2023-12-25
题目: 蛇梯棋
链接: https://leetcode-cn.com/problems/snakes-and-ladders/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ans = 0
        n = len(board)

        def get_jump(num: int):
            x, y = (num - 1) // n, (num - 1) % n
            if x & 1:
                return board[n - 1 - x][n - 1 - y]
            else:
                return board[n - 1 - x][y]

        q = deque()
        q.append((1, 0))

        while q:
            cur_pos, step = q.popleft()
            nxts = [i for i in range(cur_pos + 1, min(cur_pos + 6, n ** 2) + 1)]
            flags = [False for _ in range(len(nxts))]

            for i in len(nxts):
                true_nxt = get_jump(nxts[i])
                if true_nxt == -1:
                    true_nxt = nxts[i]
                if true_nxt != nxts[i]:
                    flags[i] = True
            
            for i in len(nxts):
                
                

            



        



        


"""
--TESTCASE BEGIN--
TestCase 0: [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
TestCase 1: [[-1,-1],[-1,3]]
--TESTCASE END--
""" 
