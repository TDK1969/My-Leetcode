'''
Descripttion: 
version: 
Author: TDK
Date: 2023-11-08 19:08:46
LastEditors: TDK 793065367@qq.com
LastEditTime: 2023-11-16 00:35:42
'''
"""
日期: 2023-11-08
题目: 二叉树展开为链表
链接: https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                precessor = nxt = cur.left
                while precessor.right:
                    precessor = precessor.right
                precessor.right = cur.right
                cur.right = nxt
                cur.left = None
            cur = cur.right


root = TreeNode(1, TreeNode(2))
Solution().flatten(root)

