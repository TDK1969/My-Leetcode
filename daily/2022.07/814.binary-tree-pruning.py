"""
日期: 2022-07-21
题目: 二叉树剪枝
链接: https://leetcode-cn.com/problems/binary-tree-pruning/
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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if not root.left and not root.right:
                if root.val == 1:
                    return root
                else:
                    return None
            else:
                if root.left:
                    root.left = self.pruneTree(root.left)
                if root.right:
                    root.right = self.pruneTree(root.right)
                
                if not root.left and not root.right and root.val == 0:
                    return None
                else:
                    return root
        
        return None