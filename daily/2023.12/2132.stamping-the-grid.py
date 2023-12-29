"""
日期: 2023-12-14
题目: 用邮票贴满网格图
链接: https://leetcode-cn.com/problems/stamping-the-grid/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:

"""
--TESTCASE BEGIN--
TestCase 0: [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]],4,3
TestCase 1: [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],2,2
--TESTCASE END--
""" 
