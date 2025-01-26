"""
日期: 2024-10-27
题目: 冗余连接
链接: https://leetcode.cn/problems/redundant-connection/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Middle:
    def __init__(self, s: Set[int]):
        self.s = s
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 并查集
        n = len(edges)
        parents = [i for i in range(n + 1)]

        def find(x: int) -> int:
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x1: int, x2: int):
            parents[find(x1)] = find(x2)
        
        for x, y in edges:
            if find(x) != find(y):
                union(x, y)
            else:
                return [x, y]
        
        return []


print(Solution().findRedundantConnection([[16,25],[7,9],[3,24],[10,20],[15,24],[2,8],[19,21],[2,15],[13,20],[5,21],[7,11],[6,23],[7,16],[1,8],[17,20],[4,19],[11,22],[5,11],[1,16],[14,20],[1,4],[22,23],[12,20],[15,18],[12,16]]))
                

        

"""
--TESTCASE BEGIN--
TestCase 0: [[1,2],[1,3],[2,3]]
TestCase 1: [[1,2],[2,3],[3,4],[1,4],[1,5]]
--TESTCASE END--
""" 
