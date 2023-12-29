"""
日期: 2023-12-24
题目: 二叉搜索树的最小绝对差
链接: https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 二叉搜索树的中序遍历是递增的
        ans = float("inf")
        pre = -float("inf")
        def dfs(root: Optional[TreeNode]):
            if root.left:
                dfs(root.left)
            nonlocal ans, pre
            ans = min(ans, root.val - pre)
            pre = root.val
            if root.right:
                dfs(root.right)
        
        dfs(root)
        return ans




"""
--TESTCASE BEGIN--
TestCase 0: [4,2,6,1,3]
TestCase 1: [1,0,48,None,None,12,49]
--TESTCASE END--
""" 

print(Solution().getMinimumDifference(create_tree([4,2,6,1,3])))