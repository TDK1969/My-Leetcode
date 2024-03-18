"""
日期: 2024-01-19
题目: 排序链表
链接: https://leetcode-cn.com/problems/sort-list/
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = fast = ListNode(-1, head)
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tail_head = slow.next
        slow.next = None

        p = self.sortList(head)
        q = self.sortList(tail_head)
        pointer = ListNode(-1)
        s = pointer

        while p and q:
            if p.val < q.val:
                s.next = p
                p = p.next
            else:
                s.next = q
                q = q.next
            s = s.next
        if p:
            s.next = p
        else:
            s.next = q
        
        return pointer.next
        
        
show_list(Solution().sortList(create_list([])))

"""
--TESTCASE BEGIN--
TestCase 0: [4,2,1,3]
TestCase 1: [-1,5,3,4,0]
TestCase 2: []
--TESTCASE END--
""" 
