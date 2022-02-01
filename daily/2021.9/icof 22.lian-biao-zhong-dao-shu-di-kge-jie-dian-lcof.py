# Definition for singly-linked list.
from collections import defaultdict
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = head
        while k:
            fast = fast.next
            k -= 1
        slow = head
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
