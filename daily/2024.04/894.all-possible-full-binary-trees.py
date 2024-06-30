"""
日期: 2024-04-02
题目: 所有可能的真二叉树
链接: https://leetcode.cn/problems/all-possible-full-binary-trees/
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
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

"""
--TESTCASE BEGIN--
TestCase 0: 7
TestCase 1: 3
--TESTCASE END--
""" 
