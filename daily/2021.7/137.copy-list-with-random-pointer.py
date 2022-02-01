
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        tail = Node(-1)
        new_head = tail
        nodes = {}

        x = head
        count = 0
        while x:
            new_node = Node(x.val)
            nodes[x] = new_node
            count += 1
            tail.next = new_node
            tail = new_node
            x = x.next

        x = head
        y = new_head.next
        while x and y:
            if x.random:
                y.random = nodes[x.random]
            x = x.next
            y = y.next

        return new_head.next

