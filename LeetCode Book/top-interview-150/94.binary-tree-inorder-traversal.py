"""
日期: 2022-07-14
题目: 二叉树的中序遍历
链接: https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        # 定义状态:0 - 未输出左子树;1 - 已输出左子树
        if root:
            stack.append([root, 0])
        while stack:
            r, status = stack.pop()
            if status == 0:
                if r.right:
                    stack.append([r.right, 0])
                stack.append([r, 1])
                if r.left:
                    stack.append([r.left, 0])
            else:
                ans.append(r.val)

        return ans

test = Solution()
print(test.inorderTraversal())
            
