"""
日期: 2022-06-18
题目: 排序的循环链表
链接: https://leetcode-cn.com/problems/4ueAj6/
"""

from typing import *
from collections import *

# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        if head.next == head:
            head.next = node
            node.next = head
            return head
        curr = head
        next = head.next
        while next != head:
            if curr.val <= insertVal <= next.val:
                break
            if curr.val > next.val:
                if insertVal > curr.val or insertVal < next.val:
                    break
            curr = curr.next
            next = next.next
        curr.next = node
        node.next = next
        return head