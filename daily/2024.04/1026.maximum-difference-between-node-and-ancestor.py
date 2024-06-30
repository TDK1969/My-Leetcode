"""
日期: 2024-04-05
题目: 节点与其祖先之间的最大差值
链接: https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/
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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [8,3,10,1,6,None,14,None,None,4,7,13]
TestCase 1: [1,None,2,None,0,3]
--TESTCASE END--
""" 
