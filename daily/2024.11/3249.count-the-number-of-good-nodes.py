"""
日期: 2024-11-14
题目: 统计好节点的数目
链接: https://leetcode.cn/problems/count-the-number-of-good-nodes/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        children = dict()
        ans = 0
        for a, b in edges:
            if a not in children:
                children[a] = []
            if b not in children:
                children[b] = []
            children[a].append(b)
            children[b].append(a)
        
        visited = set()
        def dfs(root: int) -> int:
            nonlocal ans
            
            cnt = []
            for child in children[root]:
                if child not in visited:
                    visited.add(child)
                    cnt.append(dfs(child))

            if len(cnt) == 0 or len(set(cnt)) == 1:
                ans += 1
            

            return sum(cnt) + 1
        visited.add(0)
        dfs(0)

        return ans
print(Solution().countGoodNodes([[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]]))
"""
--TESTCASE BEGIN--
TestCase 0: [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
TestCase 1: [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]
TestCase 2: [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]
--TESTCASE END--
""" 

{{0,1},{0,2},{1,3},{1,4},{2,5},{2,6}}