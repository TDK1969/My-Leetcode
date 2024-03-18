"""
日期: 2024-02-25
题目: 二叉搜索树的最近公共祖先
链接: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

from typing import *
from collections import *
from leetcode_utils import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

"""
--TESTCASE BEGIN--
TestCase 0: [6,2,8,0,4,7,9,None,None,3,5],2,8
TestCase 1: [6,2,8,0,4,7,9,None,None,3,5],2,4
TestCase 2: [2,1],2,1
--TESTCASE END--
""" 
