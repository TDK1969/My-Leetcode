"""
日期: 2024-02-20
题目: 从前序与中序遍历序列构造二叉树
链接: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

"""
--TESTCASE BEGIN--
TestCase 0: [3,9,20,15,7],[9,3,15,20,7]
TestCase 1: [-1],[-1]
--TESTCASE END--
""" 
