"""
日期: 2024-02-17
题目: N 叉树的层序遍历
链接: https://leetcode.cn/problems/n-ary-tree-level-order-traversal/
"""

from typing import *
from collections import *
from leetcode_utils import *
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        

"""
--TESTCASE BEGIN--
TestCase 0: [1,None,3,2,4,None,5,6]
TestCase 1: [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
--TESTCASE END--
""" 
