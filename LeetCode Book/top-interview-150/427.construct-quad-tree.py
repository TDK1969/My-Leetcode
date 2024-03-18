"""
日期: 2024-01-20
题目: 建立四叉树
链接: https://leetcode-cn.com/problems/construct-quad-tree/
"""

from typing import *
from collections import *
from leetcode_utils import *

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dc(x: int, y: int, r: int) -> 'Node':
            if r == 1:
                return Node(bool(grid[x][y]), True, None, None, None, None)
            top_left = dc(x, y, r // 2)
            top_right = dc(x, y + r // 2, r // 2)
            bottom_left = dc(x + r // 2, y, r // 2)
            bottom_right = dc(x + r // 2, y + r // 2, r // 2)

            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and \
            top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                return Node(top_left.val, True, None, None, None, None)
            else:
                return Node(top_left.val, False, top_left, top_right, bottom_left, bottom_right)
        
        return dc(0, 0, len(grid))
        

Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
"""
--TESTCASE BEGIN--
TestCase 0: [[0,1],[1,0]]
TestCase 1: [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
--TESTCASE END--
""" 
