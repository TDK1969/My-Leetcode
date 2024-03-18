'''
Descripttion: 
version: 
Author: TDK
Date: 2023-11-09 20:37:58
LastEditors: TDK
LastEditTime: 2023-11-09 20:43:35
'''
"""
日期: 2023-11-09
题目: 路径总和
链接: https://leetcode-cn.com/problems/path-sum/
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)