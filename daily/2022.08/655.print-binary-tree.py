"""
日期: 2022-08-22
题目: 输出二叉树
链接: https://leetcode-cn.com/problems/print-binary-tree/
"""

from typing import *
from collections import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]: