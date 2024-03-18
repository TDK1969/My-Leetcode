"""
日期: 2022-09-14
题目: 反转链表
链接: https://leetcode-cn.com/problems/reverse-linked-list/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ori = ListNode(-1)

        t = head
        while t:
            k = t
            t = t.next
            k.next = ori.next
            ori.next = k
        
        return ori.next
            
