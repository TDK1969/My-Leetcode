"""
日期: 2023-12-04
题目: 从二叉搜索树到更大和树
链接: https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/
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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        t = 0
        def backorder(root: TreeNode):
            if root.right:
                backorder(root.right)

            nonlocal t
            root.val += t
            t = root.val

            if root.left:
                backorder(root.left)
        backorder(root)
        return root

"""
--TESTCASE BEGIN--
TestCase 0: [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
TestCase 1: [0,None,1]
--TESTCASE END--
""" 

show_tree(Solution().bstToGst(create_tree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])))


