"""
日期: 2023-12-15
题目: 反转二叉树的奇数层
链接: https://leetcode-cn.com/problems/reverse-odd-levels-of-binary-tree/
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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

"""
--TESTCASE BEGIN--
TestCase 0: [2,3,5,8,13,21,34]
TestCase 1: [7,13,11]
TestCase 2: [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
--TESTCASE END--
""" 
