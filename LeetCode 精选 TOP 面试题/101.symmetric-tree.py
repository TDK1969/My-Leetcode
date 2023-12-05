"""
日期: 2023-11-03
题目: 对称二叉树
链接: https://leetcode-cn.com/problems/symmetric-tree/
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirrorTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p and q and p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left):
                return True
            elif not p and not q:
                return True
            else:
                return False
        if root:
            return isMirrorTree(root.left, root.right)
        else:
            return root