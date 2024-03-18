"""
日期: 2024-02-29
题目: 统计可能的树根数目
链接: https://leetcode.cn/problems/count-number-of-possible-root-nodes/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [[0,1],[1,2],[1,3],[4,2]],[[1,3],[0,1],[1,0],[2,4]],3
TestCase 1: [[0,1],[1,2],[2,3],[3,4]],[[1,0],[3,4],[2,1],[3,2]],1
--TESTCASE END--
""" 
