"""
日期: 2022-07-14
题目: 合并K个升序链表
链接: https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: