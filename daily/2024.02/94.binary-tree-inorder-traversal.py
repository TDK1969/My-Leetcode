"""
日期: 2024-02-10
题目: 二叉树的中序遍历
链接: https://leetcode.cn/problems/binary-tree-inorder-traversal/
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

"""
--TESTCASE BEGIN--
TestCase 0: [1,None,2,3]
TestCase 1: []
TestCase 2: [1]
--TESTCASE END--
""" 
