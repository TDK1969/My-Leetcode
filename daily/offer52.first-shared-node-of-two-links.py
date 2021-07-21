# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set()
        x = headA
        while x:
            nodes.add(x)
            x = x.next

        y = headB
        while y:
            if y in nodes:
                return y
            y = y.next

        return None

# 双指针法
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        h1, h2 = headA, headB
        while h1 != h2:
            if not h1:
                h1 = headB
            else:
                h1 = h1.next

            if not h2:
                h2 = headA
            else:
                h2 = h2.next
        return h1