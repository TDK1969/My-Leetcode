"""
日期: 2024-06-04
题目: 在带权树网络中统计可连接服务器对数目
链接: https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:

"""
--TESTCASE BEGIN--
TestCase 0: [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]],1
TestCase 1: [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]],3
--TESTCASE END--
""" 
