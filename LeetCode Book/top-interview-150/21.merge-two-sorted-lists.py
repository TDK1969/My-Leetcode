"""
日期: 2022-07-14
题目: 合并两个有序链表
链接: https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode(0, None)
        t = pre_head
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val > p2.val:
                t.next = p2
                p2 = p2.next
                t = t.next
            else:
                t.next = p1
                p1 = p1.next
                t = t.next
        
        # 最后对剩余链表的处理可以整条链表一起处理,不需要像数组一样对每个元素进行处理
        t.next = p1 if p1 else p2
        
        return pre_head.next


