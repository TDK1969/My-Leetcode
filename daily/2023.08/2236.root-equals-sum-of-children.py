"""
日期: 2023-08-20
题目: 判断根结点是否等于子结点之和
链接: https://leetcode-cn.com/problems/root-equals-sum-of-children/
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
    def checkTree(self, root: Optional[TreeNode]) -> bool: