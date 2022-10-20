"""
日期: 2022-07-14
题目: 验证二叉搜索树
链接: https://leetcode-cn.com/problems/validate-binary-search-tree/
"""

from typing import *
from collections import *
# Definition for a binary tree node.

class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(r: Optional[self.TreeNode], low: int, high: int) -> bool:
            if not r:
                return True
            if r.val <= low or r.val >= high:
                return False
            return check(r.left, low, r.val) & check(r.right, r.val, high)
        boundary = 2 ** 31 + 1
        return check(root, -boundary, boundary)
