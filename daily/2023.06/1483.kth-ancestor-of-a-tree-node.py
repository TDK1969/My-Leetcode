"""
日期: 2023-06-12
题目: 树节点的第 K 个祖先
链接: https://leetcode-cn.com/problems/kth-ancestor-of-a-tree-node/
"""

from typing import *
from collections import *

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.log = 16
        dp = [[-1 for _ in range(self.log)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = parent[i]
        
        for k in range(1, self.log):
            for i in range(n):
                if dp[i][k - 1] != -1:
                    dp[i][k] = dp[dp[i][k - 1]][k - 1]
        self.dp = dp

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.log):
            if (k >> j) & 1:
                node = self.dp[node][j]
            if node == -1:
                return -1
        return node

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.log = 16
        self.ancestors = [[-1] * self.log for _ in range(n)]
        for i in range(n):
            self.ancestors[i][0] = parent[i]
        for j in range(1, self.log):
            for i in range(n):
                if self.ancestors[i][j - 1] != -1:
                    self.ancestors[i][j] = self.ancestors[self.ancestors[i][j - 1]][j - 1]   

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.log):
            if (k>>j) & 1: 
                node = self.ancestors[node][j]
                if node == -1:
                    return -1
        return node




# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)