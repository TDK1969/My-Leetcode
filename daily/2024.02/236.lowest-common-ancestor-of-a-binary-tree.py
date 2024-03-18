"""
日期: 2024-02-09
题目: 二叉树的最近公共祖先
链接: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
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
TestCase 0: [3,5,1,6,2,0,8,None,None,7,4],5,1
TestCase 1: [3,5,1,6,2,0,8,None,None,7,4],5,4
TestCase 2: [1,2],1,2
--TESTCASE END--
""" 
