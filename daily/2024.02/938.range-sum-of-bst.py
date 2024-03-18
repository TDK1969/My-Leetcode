"""
日期: 2024-02-26
题目: 二叉搜索树的范围和
链接: https://leetcode.cn/problems/range-sum-of-bst/
"""

from typing import *
from collections import *
from leetcode_utils import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

print(Solution().rangeSumBST(create_tree([10,5,15,3,7,None,18]), 7, 15))
"""
--TESTCASE BEGIN--
TestCase 0: [10,5,15,3,7,None,18],7,15
TestCase 1: [10,5,15,3,7,13,18,1,None,6],6,10
--TESTCASE END--
""" 
