"""
日期: 2022-09-10
题目: 修剪二叉搜索树
链接: https://leetcode-cn.com/problems/trim-a-binary-search-tree/
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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def modify(root: Optional[TreeNode], low, high) -> Optional[TreeNode]:
            if not root:
                return None
            if low <= root.val <= high:
                root.left = modify(root.left, low, root.val)
                root.right = modify(root.right, root.val, high)
                return root
            if low > root.val:
                return modify(root.right, low, high)
            if high < root.val:
                return modify(root.left, low, high)
        return modify(root, low, high)