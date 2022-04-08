"""
日期: 2022-04-08
题目: N 叉树的层序遍历
链接: https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
"""
from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        stack = deque()
        ans = []
        if root is None:
            return ans

        stack.append((root, 1))

        while stack:
            node, level = stack.popleft()
            if level > len(ans):
                ans.append([])
            ans[level - 1].append(node.val)
            for child in node.children:
                stack.append((child, level + 1))
        return ans


        