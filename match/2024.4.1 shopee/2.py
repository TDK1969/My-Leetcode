class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 旋转链表
# @param head ListNode类  
# @param k int整型  
# @return ListNode类
#
class Solution:
    def Rotate(self, head: ListNode, k: int) -> ListNode:
        # write code here
        if head is None:
            return head
        head_ptr = ListNode(-1)
        head_ptr.next = head

        l = 0
        t = head_ptr.next
        while t:
            l += 1
            t = t.next

        k = k % l
        if k == 0:
            return head

        left = right = head_ptr.next
        for _ in range(k):
            right = right.next
        
        while right.next:
            right = right.next
            left = left.next
        right.next = head_ptr.next
        head_ptr.next = left.next
        left.next = None

        return head_ptr.next
