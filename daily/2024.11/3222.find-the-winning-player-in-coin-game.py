"""
日期: 2024-11-05
题目: 求出硬币游戏的赢家
链接: https://leetcode.cn/problems/find-the-winning-player-in-coin-game/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        return "Alice" if min(x, y // 4) & 1 else "Bob"

"""
--TESTCASE BEGIN--
TestCase 0: 2,7
TestCase 1: 4,11
--TESTCASE END--
""" 
