"""
日期: 2024-11-30
题目: 判断是否可以赢得数字游戏
链接: https://leetcode.cn/problems/find-if-digit-game-can-be-won/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s0 = 0
        s1 = 0
        s2 = 0
        for num in nums:
            if num < 10:
                s1 += num
            elif num < 100:
                s2 += num
            s0 += num
        
        return s1 * 2 > s0 or s2 * 2 > s0

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,4,10]
TestCase 1: [1,2,3,4,5,14]
TestCase 2: [5,5,5,25]
--TESTCASE END--
""" 
