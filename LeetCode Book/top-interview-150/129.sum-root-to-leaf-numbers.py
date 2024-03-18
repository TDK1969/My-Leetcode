"""
日期: 2023-11-09
题目: 求根节点到叶节点数字之和
链接: https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], pre: int) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return pre * 10 + node.val
            else:
                return dfs(node.left, pre * 10 + node.val) + dfs(root.right, pre * 10 + node.val)
        
        return dfs(root, 0)
            

        

        

