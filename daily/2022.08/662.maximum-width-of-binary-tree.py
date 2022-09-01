"""
日期: 2022-08-27
题目: 二叉树最大宽度
链接: https://leetcode-cn.com/problems/maximum-width-of-binary-tree/
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int: