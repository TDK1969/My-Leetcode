"""
日期: 2022-09-14
题目: 排序链表
链接: https://leetcode-cn.com/problems/sort-list/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sort_func(head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
            # 对[head, tail)范围进行排序
            # 边界条件: 节点数为0或者为1
            if not head:
                return None
            if head.next == tail:
                head.next = None
                return head
            
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sort_func(head, mid), sort_func(mid, tail))
        
        def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            ori = ListNode(-1)
            t = ori

            i, j = l1, l2
            while i and j:
                if i.val < j.val:
                    t.next = i
                    i = i.next
                else:
                    t.next = j
                    j = j.next
                t = t.next

            if i:
                t.next = i
            
            if j:
                t.next = j
            
            t.next = None
            return ori.next
        
        return sort_func(head, None)



            
a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
d = ListNode(3)
a.next = b
b.next = c
c.next = d
test = Solution()
print(test.sortList(a))