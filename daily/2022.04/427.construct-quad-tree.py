"""
日期: 2022-04-29
题目: 建立四叉树
链接: https://leetcode-cn.com/problems/construct-quad-tree/
"""
from typing import List
from collections import deque


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
        def dfs(x:int, y:int, length: int) -> 'Node':
            if length == 1:
                return Node(True if grid[x][y] == 1 else False, True, None, None, None, None)
            else:
                next_length = length >> 1
                temp = Node(False, False, dfs(x, y, next_length), dfs(x, y + next_length, next_length), dfs(x + next_length, y, next_length), dfs(x + next_length, y + next_length, next_length))
                if temp.topLeft.isLeaf and temp.topRight.isLeaf and temp.bottomLeft.isLeaf and temp.bottomRight.isLeaf:
                    if temp.topLeft.val == temp.topRight.val == temp.bottomLeft.val == temp.bottomRight.val:
                        temp.isLeaf = True
                        temp.val = temp.topLeft.val
                        temp.bottomLeft = temp.bottomRight = temp.topLeft = temp.topRight = None
                return temp
        return dfs(0, 0, len(grid))

def print_quard_tree(root: 'Node'):
    queue = deque()
    queue.append(root)

    while queue:
        temp: Node = queue.popleft()
        print([temp.isLeaf, temp.val])
        if not temp.isLeaf:
            queue.append(temp.topLeft)
            queue.append(temp.topRight)
            queue.append(temp.bottomLeft)
            queue.append(temp.bottomRight)

test = Solution()
print_quard_tree(test.construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]))