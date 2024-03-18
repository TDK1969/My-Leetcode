"""
日期: 2024-02-21
题目: 从中序与后序遍历序列构造二叉树
链接: https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""

from typing import *
from collections import *
from leetcode_utils import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

"""
--TESTCASE BEGIN--
TestCase 0: [9,3,15,20,7],[9,15,7,20,3]
TestCase 1: [-1],[-1]
--TESTCASE END--
""" 
