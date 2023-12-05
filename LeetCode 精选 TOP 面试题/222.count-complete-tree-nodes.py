'''
Descripttion: 
version: 
Author: TDK
Date: 2023-11-15 18:08:32
LastEditors: TDK
LastEditTime: 2023-11-15 18:40:27
'''
"""
日期: 2023-11-15
题目: 完全二叉树的节点个数
链接: https://leetcode-cn.com/problems/count-complete-tree-nodes/
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        l = 0
        cur = root
        while cur:
            l += 1
            cur = cur.right

        def check(num: int) -> bool:
            # 0左1右
            p = root
            for i in range(l - 1, -1, -1):
                if num & (1 << i):
                    p = p.right
                else:
                    p = p.left
            return p is not None

        left = 0
        right = 2 ** l
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        
        return 2 ** l - 1 + right

tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(Solution().countNodes(tree))