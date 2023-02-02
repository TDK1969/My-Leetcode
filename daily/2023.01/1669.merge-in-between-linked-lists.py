"""
日期: 2023-01-30
题目: 合并两个链表
链接: https://leetcode-cn.com/problems/merge-in-between-linked-lists/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        