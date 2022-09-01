"""
日期: 2022-08-30
题目: 最大二叉树 II
链接: https://leetcode-cn.com/problems/maximum-binary-tree-ii/
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
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if root.val < val:
            return TreeNode(val, root)
        if root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root

            

