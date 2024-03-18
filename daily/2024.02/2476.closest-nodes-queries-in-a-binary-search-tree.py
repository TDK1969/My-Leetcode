"""
日期: 2024-02-24
题目: 二叉搜索树最近节点查询
链接: https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/
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
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

"""
--TESTCASE BEGIN--
TestCase 0: [6,2,13,1,4,9,15,None,None,None,None,None,None,14],[2,5,16]
TestCase 1: [4,None,9],[3]
--TESTCASE END--
""" 
