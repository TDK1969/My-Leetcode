# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        if not root.left:
            return root

        nodes = []
        r = root
        while r:
            nodes.append(r)
            r = r.left
        
        nodes = nodes[::-1]
        new_root = TreeNode(nodes[0].val)
        t = new_root
        for node in nodes[1:]:
            print(node)
            new_right = TreeNode(node.val)
            if node.right:
                new_left = TreeNode(node.right.val)
            else:
                new_left = None
            t.left = new_left
            t.right = new_right
            t = t.right
        return new_root
        
t = TreeNode(1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(5)), right=TreeNode(4)))
test = Solution()
print(test.upsideDownBinaryTree(t))