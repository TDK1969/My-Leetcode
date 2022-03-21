"""
题目: 两数之和 IV - 输入 BST
链接: https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        value = set()

        stack = []

        if root is not None:
            stack.append(root)
            value.add(root.val)
        
        while stack:
            temp = stack.pop()
            if temp.left is not None:
                if k - temp.left.val in value:
                    return True
                value.add(temp.left.val)
                stack.append(temp.left)
            if temp.right is not None:
                if k - temp.right.val in value:
                    return True
                value.add(temp.right.val)
                stack.append(temp.right)

        return False
            
                

