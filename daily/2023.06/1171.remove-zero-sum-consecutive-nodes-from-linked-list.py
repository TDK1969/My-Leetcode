"""
日期: 2023-06-11
题目: 从链表中删去总和值为零的连续节点
链接: https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(0, head)
        pre = dict()
        s = 0
        t = h
        while t:
            s += t.val
            pre[s] = t
            t = t.next
        
        s = 0
        t = h
        while t:
            s += t.val
            t.next = pre[s].next
            t = t.next
        
        return h.next





