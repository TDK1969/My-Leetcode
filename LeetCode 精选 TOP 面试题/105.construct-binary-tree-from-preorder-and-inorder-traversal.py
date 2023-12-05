"""
日期: 2023-11-02
题目: 从前序与中序遍历序列构造二叉树
链接: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_val2index = {val:index for index, val in enumerate(inorder)}

        def dfs(preorder_start: int, preorder_end: int, inorder_start: int, inorder_end: int)  -> Optional[TreeNode]:
            # 判断None
            if preorder_start >= preorder_end:
                return None
            
            root = preorder[preorder_start]
            root_node = TreeNode(root)
            # 使用哈希表获取根节点的下标
            root_inorder_index = in_val2index[root]
            root_node.left = dfs(preorder_start + 1, preorder_start + 1 + root_inorder_index - inorder_start, inorder_start, root_inorder_index)
            root_node.right = dfs(preorder_start + root_inorder_index - inorder_start + 1, preorder_end, root_inorder_index + 1, inorder_end)
            return root_node
    
        return dfs(0, len(preorder), 0, len(inorder))



#tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
a = Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
print(a)