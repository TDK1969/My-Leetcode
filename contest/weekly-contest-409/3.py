from typing import List

class Node:
    def __init__(self, pre: "Node", nxt: "Node", value: int) -> None:
        self.value = value
        self.pre = pre
        self.nxt = nxt

class LinkList:

    def __init__(self, n: int):
        self.n = n
        self.head = Node(None, None, -1)
        self.tail = Node(None, None, -1)
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.d = {}
        self.init_linklist(n)

    def init_linklist(self, n: int):
        for i in range(n):
            node = Node(self.tail.pre, self.tail, i)
            self.d[i] = node
            self.tail.pre.nxt = node
            self.tail.pre = node
        
    def update(self, start: int, end: int):
        start_node: Node = self.d.get(start, None)
        end_node: Node = self.d.get(end, None)
        if start_node is None or end_node is None:
            # 被其他范围包围，不需要考虑
            return
        # 删除start到end之间的节点
        pre = start_node
        nxt = start_node.nxt
        while nxt != end_node:
            # 删除nxt
            self.d.pop(nxt.value)
            nxt.nxt.pre = pre
            pre.nxt = nxt.nxt
            nxt = pre.nxt
    
    def get_path(self):
        return len(self.d) - 1
        
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ll = LinkList(n)
        ans = []
        for start, end in queries:
            ll.update(start, end)
            ans.append(ll.get_path())
        return ans
    

print(Solution().shortestDistanceAfterQueries(n = 4, queries = [[0, 2], [0, 3]]))
