"""
日期: 2022-07-14
题目: 验证二叉搜索树
链接: https://leetcode-cn.com/problems/validate-binary-search-tree/
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool: