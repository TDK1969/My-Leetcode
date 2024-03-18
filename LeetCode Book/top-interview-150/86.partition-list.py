"""
日期: 2023-11-02
题目: 分隔链表
链接: https://leetcode-cn.com/problems/partition-list/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        smaller = ListNode(-1, None)
        larger = ListNode(-1, None)
        s, l = smaller, larger

        p = head
        while p:
            if p.val < x:
                s.next = p
                s = s.next
            else:
                l.next = p
                l = l.next

            p = p.next
        
        s.next = larger.next
        l.next = None
        return smaller.next
    

node = ListNode(6)
ans = Solution().partition(node, 3)
while ans:
    print(ans.val, "->", end="")
    ans = ans.next
                
                
