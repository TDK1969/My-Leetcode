"""
日期: 2024-02-23
题目: 二叉树中的第 K 大层和
链接: https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/
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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: [5,8,9,2,1,3,7,4,6],2
TestCase 1: [1,2,None,3],1
--TESTCASE END--
""" 
