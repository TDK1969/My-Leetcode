"""
日期: 2023-11-02
题目: 旋转链表
链接: https://leetcode-cn.com/problems/rotate-list/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        head_ptr = ListNode(-1, head)
        l = 0
        t = head_ptr.next
        while t:
            l += 1
            t = t.next
        
        k = k % l
        if k == 0:
            return head_ptr.next
        left = right = head_ptr.next
        for _ in range(k):
            right = right.next

        while right.next:
            left = left.next
            right = right.next
        
        right.next = head_ptr.next
        head_ptr.next = left.next
        left.next = None

        return head_ptr.next

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
ans = Solution().rotateRight(node, 5)
while ans:
    print(ans.val, "->", end="")
    ans = ans.next