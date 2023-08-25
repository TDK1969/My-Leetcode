"""
日期: 2023-06-24
题目: 检查平衡性
链接: https://leetcode-cn.com/problems/check-balance-lcci/
"""

from typing import *
from collections import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_balance_return_height(root: TreeNode) -> Tuple[bool, int]:
            if root is None:
                return (True, 0)
            left_balance, left_height = check_balance_return_height(root.left)
            right_balance, right_height = check_balance_return_height(root.right)
            if left_balance and right_balance and abs(left_height - right_height) <= 1:
                return (True, max(left_height, right_height) + 1)
            else:
                return (False, max(left_height, right_height) + 1)
        return check_balance_return_height(root)[0]


root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, None)))
test = Solution()
print(test.isBalanced(root))