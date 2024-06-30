"""
日期: 2024-04-03
题目: 找出克隆二叉树中的相同节点
链接: https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
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
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        

"""
--TESTCASE BEGIN--
TestCase 0: [7,4,3,None,None,6,19],3
TestCase 1: [7],7
TestCase 2: [8,None,6,None,5,None,4,None,3,None,2,None,1],4
--TESTCASE END--
""" 
