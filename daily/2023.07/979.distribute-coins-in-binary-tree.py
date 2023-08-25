"""
日期: 2023-07-14
题目: 在二叉树中分配硬币
链接: https://leetcode-cn.com/problems/distribute-coins-in-binary-tree/
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
    def distributeCoins(self, root: Optional[TreeNode]) -> int: