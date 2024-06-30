"""
日期: 2024-05-19
题目: 找出数组游戏的赢家
链接: https://leetcode.cn/problems/find-the-winner-of-an-array-game/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        winTerm = 0
        winner = arr[0]
        n = len(arr)
        for i in range(1, n):
            if arr[i] > winner:
                winner = arr[i]
                winTerm = 1
            else:
                winTerm += 1
            if winTerm == k:
                break
        return winner

print(Solution().getWinner([3,2,1],10))
"""
--TESTCASE BEGIN--
TestCase 0: [2,1,3,5,4,6,7],2
TestCase 1: [3,2,1],10
--TESTCASE END--
""" 
