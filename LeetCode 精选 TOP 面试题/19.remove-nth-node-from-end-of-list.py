"""
日期: 2022-07-14
题目: 删除链表的倒数第 N 个结点
链接: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 使用前置节点,避免对头节点进行特殊处理
        pre_head = ListNode(0, head)
        left = pre_head
        right = head

        # 左指针置为前置节点,则右指针提前移动n个节点
        for _ in range(n):
            right = right.next
        
        # 左右指针同时向后移动,当右指针移动到末尾时,左指针只想需要删除的节点的前一个结点
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return pre_head.next

        