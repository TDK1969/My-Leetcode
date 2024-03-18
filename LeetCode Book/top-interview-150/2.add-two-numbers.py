"""
日期: 2022-07-14
题目: 两数相加
链接: https://leetcode-cn.com/problems/add-two-numbers/
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
        num1 = []
        t = l1
        while t:
            num1.append(t.val)
            t = t.next
        
        num2 = []
        t = l2
        while t:
            num2.append(t.val)
            t = t.next
        
        flag = 0
        i = 0
        num = []
        while i < len(num1) and i < len(num2):
            num.append((num1[i] + num2[i] + flag) % 10)
            flag = (num1[i] + num2[i] + flag) // 10
            i += 1
        while i < len(num1):
            num.append((num1[i] + flag) % 10)
            flag = (num1[i] + flag) // 10
            i += 1
        while i < len(num2):
            num.append((num2[i] + flag) % 10)
            flag = (num2[i] + flag) // 10
            i += 1
        if flag:
            num.append(1)

        ans = ListNode(num[0])
        t = ans
        for i in ans[1:]:
            t.next = ListNode(i)
            t = t.next
        return ans
            
