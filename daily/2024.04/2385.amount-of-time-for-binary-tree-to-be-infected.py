"""
日期: 2024-04-24
题目: 感染二叉树需要的总时间
链接: https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/
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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [1,5,3,None,4,10,6,9,2],3
TestCase 1: [1],1
--TESTCASE END--
""" 
