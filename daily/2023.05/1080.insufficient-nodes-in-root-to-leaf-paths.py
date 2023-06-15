"""
日期: 2023-05-22
题目: 根到叶路径上的不足节点
链接: https://leetcode-cn.com/problems/insufficient-nodes-in-root-to-leaf-paths/
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
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]: