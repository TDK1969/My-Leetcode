"""
日期: 2022-05-30
题目: 从根到叶的二进制数之和
链接: https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/
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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.temp = 0

        def dfs(root: TreeNode):
            if root:
                self.temp = (self.temp << 1) + root.val
            if root.left:
                dfs(root.left)
                self.temp = self.temp >> 1
            if root.right:
                dfs(root.right)
                self.temp = self.temp >> 1
            if not root.right and not root.left:
                self.ans += self.temp
        dfs(root)
        return self.ans
