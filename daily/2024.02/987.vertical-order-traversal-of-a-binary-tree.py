"""
日期: 2024-02-13
题目: 二叉树的垂序遍历
链接: https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/
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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

"""
--TESTCASE BEGIN--
TestCase 0: [3,9,20,None,None,15,7]
TestCase 1: [1,2,3,4,5,6,7]
TestCase 2: [1,2,3,4,6,5,7]
--TESTCASE END--
""" 
