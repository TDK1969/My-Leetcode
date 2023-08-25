"""
日期: 2023-07-03
题目: 两数相加 II
链接: https://leetcode-cn.com/problems/add-two-numbers-ii/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        p = l1
        while p:
            num1 = num1 * 10 + p.val
            p = p.next
        
        num2 = 0
        p = l2
        while p:
            num2 = num2 * 10 + p.val
            p = p.next
        
        res = num1 + num2
        if res == 0:
            return ListNode(val=0, next=None)

        k = res
        p = None
        while k:
            k, x = k // 10, k % 10
            temp = ListNode(x, p)
            p = temp
        
        return p

test = Solution()
l1 = ListNode(1, ListNode(2, ListNode(3, None)))
print(test.addTwoNumbers(l1, l1))

