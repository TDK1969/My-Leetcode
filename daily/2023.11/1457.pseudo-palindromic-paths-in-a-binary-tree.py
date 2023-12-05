"""
日期: 2023-11-25
题目: 二叉树中的伪回文路径
链接: https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
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
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [2,3,1,3,1,None,1]
TestCase 1: [2,1,1,1,3,None,None,None,None,None,1]
TestCase 2: [9]
--TESTCASE END--
""" 
