"""
题目: 计算布尔二叉树的值
链接: https://leetcode-cn.com/problems/evaluate-boolean-binary-tree/
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
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root:
            if root.left and root.right:
                if root.val == 2:
                    return self.evaluateTree(root.left) or self.evaluateTree(root.right)
                else:
                    return self.evaluateTree(root.left) and self.evaluateTree(root.right)
            else:
                if root.val == 0:
                    return False
                else:
                    return True