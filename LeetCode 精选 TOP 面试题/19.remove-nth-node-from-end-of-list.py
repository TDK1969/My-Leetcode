"""
日期: 2022-07-14
题目: 删除链表的倒数第 N 个结点
链接: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode: