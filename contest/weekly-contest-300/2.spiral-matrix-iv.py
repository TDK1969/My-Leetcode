"""
题目: 螺旋矩阵 IV
链接: https://leetcode-cn.com/problems/spiral-matrix-iv/
"""

from typing import *
from collections import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next

        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        dirs = [1, 1, -1, -1]
        changes = [1, -1, -1, 1]
        limit = [n - 1, m - 1, 0, 0]

        pos = [0, 0]
        dir = 0
        for i in nums:
            matrix[pos[0]][pos[1]] = i
            if dir <= 1 and pos[((dir & 1) + 1) % 2] + dirs[dir] <= limit[dir] or \
                dir > 1 and pos[((dir & 1) + 1) % 2] + dirs[dir] >= limit[dir]:
                pos[((dir & 1) + 1) % 2] += dirs[dir]
            else:
                limit[dir - 1] += changes[dir]
                dir = (dir + 1) % 4
                if dir <= 1 and pos[((dir & 1) + 1) % 2] + dirs[dir] <= limit[dir] or \
                    dir > 1 and pos[((dir & 1) + 1) % 2] + dirs[dir] >= limit[dir]:
                    pos[((dir & 1) + 1) % 2] += dirs[dir]
        return matrix

    def spiralMatrix1(self, m: int, n: int, head: List[int]) -> List[List[int]]:
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next

        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        dirs = [1, 1, -1, -1]
        changes = [1, -1, -1, 1]
        limit = [n - 1, m - 1, 0, 0]

        pos = [0, 0]
        dir = 0
        for i in nums:
            matrix[pos[0]][pos[1]] = i
            if dir <= 1 and pos[((dir & 1) + 1) % 2] + dirs[dir] <= limit[dir] or \
                dir > 1 and pos[((dir & 1) + 1) % 2] + dirs[dir] >= limit[dir]:
                pos[((dir & 1) + 1) % 2] += dirs[dir]
            else:
                limit[dir - 1] += changes[dir]
                dir = (dir + 1) % 4
                if dir <= 1 and pos[((dir & 1) + 1) % 2] + dirs[dir] <= limit[dir] or \
                    dir > 1 and pos[((dir & 1) + 1) % 2] + dirs[dir] >= limit[dir]:
                    pos[((dir & 1) + 1) % 2] += dirs[dir]
        return matrix

test = Solution()
print(test.spiralMatrix1(m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]))
        
                



