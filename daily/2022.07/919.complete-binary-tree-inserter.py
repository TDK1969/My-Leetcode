"""
日期: 2022-07-25
题目: 完全二叉树插入器
链接: https://leetcode-cn.com/problems/complete-binary-tree-inserter/
"""

from typing import *
from collections import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        q = deque()
        
        q.append(root)

        while True:
            t = q[0]
            if t.left and t.right:
                q.append(t.left)
                q.append(t.right)
                q.popleft()
            elif t.left and not t.right:
                q.append(t.left)
                break
            else:
                break
        
        self.q = q

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        self.q.append(new_node)
        t = self.q[0]
        if not t.left:
            t.left = new_node
        else:
            t.right = new_node
            self.q.popleft()
        return t.val

        q = deque()
        q.append(self.root)

    def get_root(self) -> TreeNode:
        return self.root



# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()