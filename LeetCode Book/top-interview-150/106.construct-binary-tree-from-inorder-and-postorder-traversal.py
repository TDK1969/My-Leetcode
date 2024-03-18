'''
Descripttion: 
version: 
Author: TDK
Date: 2023-11-08 18:48:47
LastEditors: TDK
LastEditTime: 2023-11-08 19:23:46
'''
"""
日期: 2023-11-08
题目: 从中序与后序遍历序列构造二叉树
链接: https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_val2index = {v:i for i, v in enumerate(inorder)}

        def dfs(post_start: int, post_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            if in_start >= in_end or post_start >= post_end:
                return None
            
            root_val = postorder[post_end - 1]
            root_index = inorder_val2index[root_val]
            root_node = TreeNode(root_val)
            left_length = root_index - in_start
            root_node.left = dfs(post_start, post_start + left_length, in_start, root_index)
            root_node.right = dfs(post_start + left_length, post_end - 1, root_index + 1, in_end)
            return root_node 
        
        return dfs(0, len(postorder), 0, len(inorder))
        
print(Solution().buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]))