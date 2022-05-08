"""
题目: 统计值等于子树平均值的节点数
链接: https://leetcode-cn.com/problems/count-nodes-equal-to-average-of-subtree/
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
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def calc(root: "TreeNode") -> Tuple[int, int]:
            (left_sum, left_count) = calc(root.left) if root.left else (0, 0)
            (right_sum, right_count) = calc(root.right) if root.right else (0, 0)
            if (left_sum + right_sum + root.val) // (left_count + right_count + 1) == root.val:
                self.ans += 1
            return (left_sum + right_sum + root.val, left_count + right_count + 1)
        calc(root)
        return self.ans
