"""
日期: 2022-05-24
题目: 单值二叉树
链接: https://leetcode-cn.com/problems/univalued-binary-tree/
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
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp.val != val:
                return False
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        return True