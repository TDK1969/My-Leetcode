"""
日期: 2024-02-22
题目: 根据前序和后序遍历构造二叉树
链接: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,4,5,3,6,7],[4,5,2,6,7,3,1]
TestCase 1: [1],[1]
--TESTCASE END--
""" 
