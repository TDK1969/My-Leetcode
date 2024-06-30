"""
日期: 2024-06-13
题目: 子序列最大优雅度
链接: https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [[3,2],[5,1],[10,1]],2
TestCase 1: [[3,1],[3,1],[2,2],[5,3]],3
TestCase 2: [[1,1],[2,1],[3,1]],3
--TESTCASE END--
""" 
