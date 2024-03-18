"""
日期: 2024-01-20
题目: 合并 K 个升序链表
链接: https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""

from typing import *
from collections import *
from leetcode_utils import *
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class MyList:
            def __init__(self, l: Optional[ListNode]) -> None:
                self.l = l
            def __lt__(self, other):
                return self.l.val < other.l.val
            def __le__(self, other):
                return self.l.val <= other.l.val
        
        ans = ListNode(-1)
        p = ans
        h = []
        heapq.heapify(h)

        for l in lists:
            if l:
                heapq.heappush(h, MyList(l))
        
        while h:
            cnt = heapq.heappop(h)
            p.next = cnt.l
            p = p.next
            cnt.l = cnt.l.next

            if cnt.l:
                heapq.heappush(h, cnt)
        
        p.next = None
        return ans.next


show_list(Solution().mergeKLists([create_list([1,4,5]), create_list([1,3,4]), create_list([2,6])]))
"""
--TESTCASE BEGIN--
TestCase 0: [[1,4,5],[1,3,4],[2,6]]
TestCase 1: []
TestCase 2: [[]]
--TESTCASE END--
""" 
