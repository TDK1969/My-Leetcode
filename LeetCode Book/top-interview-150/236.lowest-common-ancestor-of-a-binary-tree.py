'''
Author: TDK
Date: 2023-11-16 00:39:18
LastEditors: TDK 793065367@qq.com
LastEditTime: 2023-11-16 01:23:37
FilePath: /My-Leetcode/LeetCode 精选 TOP 面试题/236.lowest-common-ancestor-of-a-binary-tree.py
Description: 
'''
"""
日期: 2023-11-16
题目: 二叉树的最近公共祖先
链接: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

from typing import *
from collections import *
from ..py_constructor import tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        l,r = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        else:
            return l if l else r


"""
--TESTCASE BEGIN--
TestCase 0: [3,5,1,6,2,0,8,null,null,7,4],5,1
TestCase 1: [3,5,1,6,2,0,8,null,null,7,4],5,4
TestCase 2: [1,2],1,2
--TESTCASE END--
""" 
