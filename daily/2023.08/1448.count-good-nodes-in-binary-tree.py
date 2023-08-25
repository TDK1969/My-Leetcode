"""
日期: 2023-08-25
题目: 统计二叉树中好节点的数目
链接: https://leetcode-cn.com/problems/count-good-nodes-in-binary-tree/
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
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, max_val: int):
            if root is None:
                return 0
            if root.val >= max_val:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, max_val) + dfs(root.right, max_val)

        return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)

            