'''
Descripttion: 
version: 
Author: TDK
Date: 2023-11-15 11:33:08
LastEditors: TDK
LastEditTime: 2023-11-15 15:45:27
'''
"""
日期: 2023-11-15
题目: 二叉搜索树迭代器
链接: https://leetcode-cn.com/problems/binary-search-tree-iterator/
"""

from typing import *
from collections import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.mid = []
        self.cur = root
            
    def next(self) -> int:
        while self.cur:
            self.mid.append(self.cur)
            self.cur = self.cur.left
        
        self.cur = self.mid.pop()
        ans = self.cur.val
        self.cur = self.cur.right
        return ans


    def hasNext(self) -> bool:
        return self.cur is not None or self.mid



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()