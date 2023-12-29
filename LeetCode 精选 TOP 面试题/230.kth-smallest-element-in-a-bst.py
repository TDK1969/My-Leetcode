"""
日期: 2023-12-24
题目: 二叉搜索树中第K小的元素
链接: https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 1
        ans = -1
        def dfs(root: Optional[TreeNode]):
            if root.left:
                dfs(root.left)
            nonlocal i, ans
            if i == k:
                ans = root.val
            i += 1
            if root.right:
                dfs(root.right)
        
        dfs(root)
        return ans


"""
--TESTCASE BEGIN--
TestCase 0: [3,1,4,None,2],1
TestCase 1: [5,3,6,2,4,None,None,1],3
--TESTCASE END--
""" 
