"""
日期: 2022-08-17
题目: 层数最深叶子节点的和
链接: https://leetcode-cn.com/problems/deepest-leaves-sum/
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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        cur_node_nums = 1
        nxt_node_nums = 0
        cur_node_cnt = 0
        record_node_sum = 0
        cur_node_sum = 0

        while q:
            t = q.popleft()
            cur_node_cnt += 1
            cur_node_sum += t.val
            if t.left:
                q.append(t.left)
                nxt_node_nums += 1
            if t.right:
                q.append(t.right)
                nxt_node_nums += 1

            if cur_node_cnt == cur_node_nums:
                record_node_sum = cur_node_sum
                cur_node_sum = 0
                cur_node_nums = nxt_node_nums
                cur_node_cnt = 0
                nxt_node_nums = 0
        return record_node_sum
        




