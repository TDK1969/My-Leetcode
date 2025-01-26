"""
日期: 2024-12-19
题目: 找到稳定山的下标
链接: https://leetcode.cn/problems/find-indices-of-stable-mountains/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,4,5],2
TestCase 1: [10,1,10,1,10],3
TestCase 2: [10,1,10,1,10],10
--TESTCASE END--
""" 
