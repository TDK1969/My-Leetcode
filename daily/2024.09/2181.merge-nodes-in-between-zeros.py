"""
日期: 2024-09-09
题目: 合并零之间的节点
链接: https://leetcode.cn/problems/merge-nodes-in-between-zeros/
"""

from typing import *
from collections import *
from leetcode_utils import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

"""
--TESTCASE BEGIN--
TestCase 0: [0,3,1,0,4,5,2,0]
TestCase 1: [0,1,0,3,0,2,2,0]
--TESTCASE END--
""" 
