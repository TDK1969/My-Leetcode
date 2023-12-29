"""
日期: 2023-12-27
题目: 保龄球游戏的获胜者
链接: https://leetcode-cn.com/problems/determine-the-winner-of-a-bowling-game/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calc_score(player: List[int]) -> int:
            double = 0
            res = 0
            for score in player:
                if double > 0:
                    res += score * 2
                else:
                    res += score
                if score == 10:
                    double = 2
                double -= 1
            return res
        score1 = calc_score(player1)
        score2 = calc_score(player2)
        if score1 > score2:
            return 1
        elif score1 < score2:
            return 2
        else:
            return 0


"""
--TESTCASE BEGIN--
TestCase 0: [4,10,7,9],[6,5,2,3]
TestCase 1: [3,5,7,6],[8,10,10,2]
TestCase 2: [2,3],[4,1]
--TESTCASE END--
""" 
print(Solution().isWinner([2,3],[4,1]))