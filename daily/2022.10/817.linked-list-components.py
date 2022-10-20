"""
日期: 2022-10-12
题目: 链表组件
链接: https://leetcode-cn.com/problems/linked-list-components/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int: