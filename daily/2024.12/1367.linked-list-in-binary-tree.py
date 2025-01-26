"""
日期: 2024-12-30
题目: 二叉树中的链表
链接: https://leetcode.cn/problems/linked-list-in-binary-tree/
"""

from typing import *
from collections import *
from leetcode_utils import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        

"""
--TESTCASE BEGIN--
TestCase 0: [4,2,8],[1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
TestCase 1: [1,4,2,6],[1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
TestCase 2: [1,4,2,6,8],[1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
--TESTCASE END--
""" 
