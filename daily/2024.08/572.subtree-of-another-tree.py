"""
日期: 2024-08-04
题目: 另一棵树的子树
链接: https://leetcode.cn/problems/subtree-of-another-tree/
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

"""
--TESTCASE BEGIN--
TestCase 0: [3,4,5,1,2],[4,1,2]
TestCase 1: [3,4,5,1,2,None,None,None,None,0],[4,1,2]
--TESTCASE END--
""" 
