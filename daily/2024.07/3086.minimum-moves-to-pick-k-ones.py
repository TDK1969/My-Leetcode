"""
日期: 2024-07-04
题目: 拾起 K 个 1 需要的最少行动次数
链接: https://leetcode.cn/problems/minimum-moves-to-pick-k-ones/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [1,1,0,0,0,1,1,0,0,1],3,1
TestCase 1: [0,0,0,0],2,3
--TESTCASE END--
""" 
