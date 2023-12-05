"""
日期: 2023-11-03
题目: 填充每个节点的下一个右侧节点指针 II
链接: https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
"""

from typing import *
from collections import *

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur_stack = []
        nxt_stack = [root]

        while nxt_stack:
            nxt = None
            cur_stack = nxt_stack[::-1]
            nxt_stack = []
            while cur_stack:
                t = cur_stack.pop()
                t.next = nxt
                nxt = t
                
                if t.right:
                    nxt_stack.append(t.right)
                if t.left:
                    nxt_stack.append(t.left)
            
        return root
            
