"""
日期: 2022-05-11
题目: 序列化和反序列化二叉搜索树
链接: https://leetcode-cn.com/problems/serialize-and-deserialize-bst/
"""

from typing import *
from collections import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None   

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # 前序遍历
        ans = []
        
        def dfs(root: TreeNode):
            if root:
                ans.append(str(root.val))
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)

        dfs(root)

        return " ".join(ans)

        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return None

        node_vals = [int(i) for i in data.split()]
        node_vals.reverse()

        def dfs(root: TreeNode, parent_val: int) -> TreeNode:
            if node_vals:
                if node_vals[-1] < root.val:
                    root.left = dfs(TreeNode(node_vals.pop()), root.val)

            if node_vals:
                if root.val < node_vals[-1] < parent_val:
                    root.right = dfs(TreeNode(node_vals.pop()), parent_val)
                
            
            return root
        
        root = dfs(TreeNode(node_vals.pop()), 10005)
        return root


            

                





        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans