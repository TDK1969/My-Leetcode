"""
日期: 2022-05-01
题目: 两棵二叉搜索树中的所有元素
链接: https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/
"""
from typing import List
import bisect

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        def dfs1(root: TreeNode):
            if root:
                if root.left:
                    dfs1(root.left)
                ans.append(root.val)
                if root.right:
                    dfs1(root.right)
        def dfs2(root: TreeNode):
            if root:
                if root.left:
                    dfs2(root.left)
                ans.insert(bisect.bisect(ans, root.val), root.val)
                if root.right:
                    dfs2(root.right)
        dfs1(root1)
        dfs2(root2)
        return ans