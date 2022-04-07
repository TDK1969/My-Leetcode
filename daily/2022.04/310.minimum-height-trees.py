"""
日期: 2022-04-06
题目: 最小高度树
链接: https://leetcode-cn.com/problems/minimum-height-trees/
"""
from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        e = defaultdict(list)
        for edge in edges:
            e[edge[0]].append(edge[1])
            e[edge[1]].append(edge[0])
        minHeight = float("inf")
        height = 0
        treeHeight = 0
        ans = []

        def dfs(root: int):
            nonlocal height, treeHeight
            if len(e[root]) == 1 and e[root][0] in visited:
                treeHeight = max(treeHeight, height)
                return
            for nxt in e[root]:
                if nxt not in visited:
                    visited.add(nxt)
                    height += 1
                    dfs(nxt)
                    height -= 1
            return

        for i in range(n):
            visited = set()
            height = 0
            treeHeight = 0
            visited.add(i)
            dfs(i)

            if treeHeight == minHeight:
                ans.append(i)
            elif treeHeight < minHeight:
                minHeight = treeHeight
                ans = [i]
        
        return ans

test = Solution()
print(test.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))
        
        
