"""
题目: 极大极小游戏
链接: https://leetcode-cn.com/problems/min-max-game/
"""

from typing import *
from collections import *
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        cur = nums
        nxt = []
        while len(cur) > 1:
            for i in range(0, len(cur), 2):
                if i % 4 == 0:
                    nxt.append(min(cur[i], cur[i + 1]))
                else:
                    nxt.append(max(cur[i], cur[i + 1]))
            cur = nxt
            nxt = []
        return cur[0]


        
