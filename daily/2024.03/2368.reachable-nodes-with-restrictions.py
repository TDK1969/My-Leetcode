"""
日期: 2024-03-02
题目: 受限条件下可到达节点的数目
链接: https://leetcode.cn/problems/reachable-nodes-with-restrictions/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: 7,[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]],[4,5]
TestCase 1: 7,[[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]],[4,2,1]
--TESTCASE END--
""" 
