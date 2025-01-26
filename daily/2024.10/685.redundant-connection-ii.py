"""
日期: 2024-10-28
题目: 冗余连接 II
链接: https://leetcode.cn/problems/redundant-connection-ii/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n + 1)]
        ans1 = ans2 = -1

        def find(x: int) -> int:
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x1: int, x2: int):
            parents[find(x1)] = find(x2)
        
        for x, y in edges:
            if find(x) != find(y):
                union(y, x)
            else:
                ans1, ans2 = x, y
        
        return [ans1, ans2]

print(Solution().findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))
"""
--TESTCASE BEGIN--
TestCase 0: [[1,2],[1,3],[2,3]]
TestCase 1: [[1,2],[2,3],[3,4],[4,1],[1,5]]
--TESTCASE END--
""" 
