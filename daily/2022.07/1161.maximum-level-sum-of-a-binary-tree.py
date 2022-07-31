"""
日期: 2022-07-31
题目: 最大层内元素和
链接: https://leetcode-cn.com/problems/maximum-level-sum-of-a-binary-tree/
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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        level = 1
        ans = 1
        max_level_sum = root.val
        cnt_level_sum = 0
        level_node_count = 1
        nxt_node_count = 0

        q.append(root)
        
        while q:
            t = q.popleft()
            level_node_count -= 1
            cnt_level_sum += t.val

            if t.left:
                q.append(t.left)
                nxt_node_count += 1
            if t.right:
                q.append(t.right)
                nxt_node_count += 1
            
            if level_node_count == 0:
                if cnt_level_sum > max_level_sum:
                    ans = level
                    max_level_sum = cnt_level_sum
                cnt_level_sum = 0
                level_node_count = nxt_node_count
                nxt_node_count = 0
                level += 1
        return ans
