'''
Author: TDK 793065367@qq.com
Date: 2023-11-10 11:05:36
LastEditors: TDK 793065367@qq.com
LastEditTime: 2023-11-15 20:10:57
FilePath: /My-Leetcode/LeetCode 精选 TOP 面试题/124.binary-tree-maximum-path-sum.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
Descripttion: 
version: 
Author: TDK
Date: 2023-11-10 11:05:36
LastEditors: TDK
LastEditTime: 2023-11-10 12:00:02
'''
"""
日期: 2023-11-10
题目: 二叉树中的最大路径和
链接: https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -1001

        def dfs(node: Optional[TreeNode]) -> int:
            
            left_val = dfs(node.left) if node.left else 0
            right_val = dfs(node.right) if node.right else 0
            nonlocal ans
            ans = max(ans, node.val + max(0, left_val) + max(0, right_val))
            return node.val + max(max(0, left_val), max(0, right_val))
    
        dfs(root)
        return ans

tree = TreeNode(
    9,
    TreeNode(6),
    TreeNode(
        -3,
        TreeNode(
            -6
        ),
        TreeNode(
            2,
            TreeNode(
                2,
                TreeNode(
                    -6
                ),
                TreeNode(
                    -6
                )
            )
        )
    )
)
print(Solution().maxPathSum(tree))