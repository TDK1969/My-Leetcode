"""
日期: 2022-06-22
题目: 找树左下角的值
链接: https://leetcode-cn.com/problems/find-bottom-left-tree-value/
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.ans = root.val
        def dfs(root: TreeNode, depth: int):
            if root:
                if depth > self.depth:
                    self.depth = depth
                    self.ans = root.val
                if root.left:
                    dfs(root.left, depth + 1)
                if root.right:
                    dfs(root.right, depth + 1)
        dfs(root, 0)
        
        return self.ans
                
