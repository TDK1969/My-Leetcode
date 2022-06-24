"""
日期: 2022-06-24
题目: 在每个树行中找最大值
链接: https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/
"""

from typing import *
from collections import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []

        def dfs(root: TreeNode, depth: int):
            if root:
                if depth > len(self.ans):
                    self.ans.append(root.val)
                else:
                    self.ans[depth - 1] = max(self.val, self.ans[depth - 1])
                if root.left:
                    dfs(root.left, depth + 1)
                if root.right:
                    dfs(root.right, depth + 1)
        
        dfs(root, 1)
        return self.ans