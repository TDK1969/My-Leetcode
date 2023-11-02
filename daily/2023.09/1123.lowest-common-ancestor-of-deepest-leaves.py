"""
日期: 2023-09-06
题目: 最深叶节点的最近公共祖先
链接: https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves/
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
    def lcaDeepestLeaves1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = [root, 0]

        def dfs(root: TreeNode, depth: int) -> int:
            left_depth = dfs(root.left, depth + 1) if root.left else depth
            right_depth = dfs(root.right, depth + 1) if root.right else depth
            if left_depth == right_depth:
                if left_depth > ans[1]:
                    ans[0] = root
                    ans[1] = left_depth
            return max(left_depth, right_depth)
    
        dfs(root, 0)
        return ans[0]

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root: TreeNode) -> (int, TreeNode):
            if not root:
                return 0, None
            
            l_depth, l_lca = dfs(root.left)
            r_depth, r_lca = dfs(root.right)

            if l_depth > r_depth:
                return l_depth + 1, l_lca
            elif r_depth > l_depth:
                return r_depth + 1, r_lca
            else:
                return l_depth + 1, root
    
        return dfs(root)[1]



test = Solution()
r = TreeNode(1)
r.left = TreeNode(2)
r.left.left = TreeNode(3)
r.left.right = TreeNode(4)
r.left.right.left = TreeNode(5)
print(test.lcaDeepestLeaves(r).val)