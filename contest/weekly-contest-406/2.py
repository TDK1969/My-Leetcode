from typing import *
from collections import *
from leetcode_utils import *

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(-1, head)
        s = set(nums)
        p = start.next
        pre = start
        while p:
            if p.val in s:
                pre.next = p.next
            else:
                pre = pre.next
            
            p = p.next
        return start.next

