"""
日期: 2022-07-14
题目: 合并K个升序链表
链接: https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""

import heapq
from typing import *
from collections import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pre_head = ListNode(-1)

        class status:
            def __init__(self, l: Optional[ListNode]):
                self.l = l
            def __lt__(self, other):
                return self.l.val < other.l.val
            def __le__(self, other):
                return self.l.val <= other.l.val

        h = []
        heapq.heapify(h)
        for index, l in enumerate(lists):
            if l:
                heapq.heappush(h, status(l))
        
        t = pre_head
        while h:
            cnt_status = heapq.heappop(h)
            t.next = cnt_status.l
            cnt_status.l = cnt_status.l.next
            t = t.next
            if l:
                heapq.heappush(h, cnt_status)
        
        return pre_head.next
        
        
