# Definition for a binary tree node.
from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(set)

        def dfs(root: TreeNode):
            if root.left:
                graph[root.val].add(root.left.val)
                graph[root.left.val].add(root.val)
                dfs(root.left)
            if root.right:
                graph[root.val].add(root.right.val)
                graph[root.right.val].add(root.val)
                dfs(root.right)

        dfs(root)
        visited = {target.val}
        cur = [target.val]
        while k:
            next_time = []
            while cur:
                temp = cur.pop()
                for node in graph[temp]:
                    if node not in visited:
                        visited.add(node)
                        next_time.append(node)
            k -= 1
            cur = next_time
        return cur
