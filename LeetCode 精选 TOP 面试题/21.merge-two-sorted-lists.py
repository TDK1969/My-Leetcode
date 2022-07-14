"""
日期: 2022-07-14
题目: 合并两个有序链表
链接: https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: