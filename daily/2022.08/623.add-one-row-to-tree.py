"""
日期: 2022-08-05
题目: 在二叉树中增加一行
链接: https://leetcode-cn.com/problems/add-one-row-to-tree/
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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            q = deque()
            cur_depth = 1
            cur_depth_cnt = 1
            cur_cnt = 0
            q.append(root)

            while q:
                t = q.popleft()
                cur_cnt += 1
                if cur_depth != depth - 1:
                    if t.left:
                        q.append(t.left)
                    if t.right:
                        q.append(t.right)
                else:
                    n1 = TreeNode(val, t.left, None)
                    n2 = TreeNode(val, None, t.right)
                    t.left = n1
                    t.right = n2
                if cur_cnt == cur_depth_cnt:
                    cur_cnt = 0
                    cur_depth_cnt = len(q)
                    cur_depth += 1
            return root
            



