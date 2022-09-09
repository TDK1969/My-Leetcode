"""
日期: 2022-09-02
题目: 最长同值路径
链接: https://leetcode-cn.com/problems/longest-univalue-path/
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int: