"""
日期: 2022-07-08
题目: 玩筹码
链接: https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position/
"""

from typing import *
from collections import *
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(len([i for i in position if i & 1]), len([j for j in position if j & 1 != 0]))