"""
日期: 2023-09-18
题目: 打家劫舍 III
链接: https://leetcode-cn.com/problems/house-robber-iii/
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
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(root: TreeNode) -> Tuple[int, int]:
            if not root:
                return 0, 0
            left1, left2 = dfs(root.left)
            right1, right2 = dfs(root.right)
            return root.val + left2 + right2, max(left1, left2) + max(right1, right2)

        return max(dfs(root))
        