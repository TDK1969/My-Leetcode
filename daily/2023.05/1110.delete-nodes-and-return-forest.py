"""
日期: 2023-05-30
题目: 删点成林
链接: https://leetcode-cn.com/problems/delete-nodes-and-return-forest/
"""

from typing import *
from collections import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode],  to_delete: List[int]) -> List[TreeNode]:
        ans = [root]

        def dfs(root: Optional[TreeNode], target: int, pre: Optional[TreeNode],) -> bool:
            if root.val == target:
                if root.left is not None:
                    ans.append(root.left)
                if root.right is not None:
                    ans.append(root.right)
                if pre is None:
                    return False
                elif pre.left == root:
                    pre.left = None
                elif pre.right == root:
                    pre.right = None
                return True
            r1 = r2 = False
            if root.right:
                r1 = dfs(root.right, target, root)
            if root.left and not r1:
                r2 = dfs(root.right, target, root)
            return r1 or r2

        for target in to_delete:
            for index, node in enumerate(ans):
                if node.val == target:
                    l = node.left
                    r = node.right
                    
                    




            

                
