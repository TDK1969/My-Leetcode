# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *
from collections import *

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        tree_map = defaultdict(list)
        def make_map(root: Optional[TreeNode]):
            if root.left:
                tree_map[root.val].append(root.left.val)
                tree_map[root.left.val].append(root.val)
                make_map(root.left)
            if root.right:
                tree_map[root.val].append(root.right.val)
                tree_map[root.right.val].append(root.val)
                make_map(root.right)
        make_map(root)

        visited = set()
        q = deque()
        ans = 0

        visited.add(start)
        q.append(start)
        nxt_q = deque()


        while q:
            t = q.popleft()
            for nxt in tree_map[t]:
                if nxt not in visited:
                    visited.add(nxt)
                    nxt_q.append(nxt)
            if not q:
                q = nxt_q
                nxt_q = deque()
                ans += 1
        
        return ans - 1

