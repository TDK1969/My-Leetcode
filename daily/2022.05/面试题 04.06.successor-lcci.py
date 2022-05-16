"""
日期: 2022-05-16
题目: 后继者
链接: https://leetcode-cn.com/problems/successor-lcci/
"""

from typing import *
from collections import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        r, nxt = root, None
        while r:
            if p.val < r.val:
                r, nxt = r.left, r
            elif p.val > r.val:
                r, nxt = r.right, nxt
            else:
                if r.right:
                    return r.right
                else:
                    return nxt
