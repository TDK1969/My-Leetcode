"""
日期: 2022-07-14
题目: 跳跃游戏
链接: https://leetcode-cn.com/problems/jump-game/
"""

from typing import *
from collections import *
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        e = 0
        n = len(nums)
        for i in range(n - 1):
            e = max(e, nums[i])
            if e == 0:
                return False
            e -= 1
        return True