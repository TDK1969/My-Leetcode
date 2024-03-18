"""
日期: 2024-02-15
题目: 二叉树的层序遍历 II
链接: https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/
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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

"""
--TESTCASE BEGIN--
TestCase 0: [3,9,20,None,None,15,7]
TestCase 1: [1]
TestCase 2: []
--TESTCASE END--
""" 
