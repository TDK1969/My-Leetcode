"""
日期: 2022-07-15
题目: 四叉树交集
链接: https://leetcode-cn.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/
"""

from typing import *
from collections import *

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
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf == True and quadTree2.isLeaf == True:
            if quadTree1.val:
                return quadTree1
            else:
                return quadTree2
        elif quadTree1.isLeaf == True or quadTree2.isLeaf == True:
            (true_tree, false_tree) = (quadTree1, quadTree2) if quadTree1.isLeaf else (quadTree2, quadTree1)
            if true_tree.val == True:
                return true_tree
            else:
                return false_tree
        else:
            new_tree = Node(False, False, None, None, None, None)

            new_tree.topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            new_tree.topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            new_tree.bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            new_tree.bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if new_tree.topLeft.isLeaf and new_tree.topRight.isLeaf and new_tree.bottomLeft.isLeaf and new_tree.bottomRight.isLeaf:
                if new_tree.topLeft.val == new_tree.topRight.val == new_tree.bottomLeft.val == new_tree.bottomRight.val:
                    new_tree.isLeaf = True
                    new_tree.val = new_tree.topLeft.val
                    new_tree.topLeft = new_tree.topRight = new_tree.bottomLeft = new_tree.bottomRight = None

            return new_tree


            