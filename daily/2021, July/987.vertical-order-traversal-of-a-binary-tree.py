# Definition for a binary tree node.
from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        vertical = defaultdict(list)

        def dfs(node: TreeNode, col: int, row: int) -> None:
            vertical[col].append((row, node.val))
            if node.left:
                dfs(node.left, col - 1, row + 1)
            if node.right:
                dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)
        vertical = list(vertical.items())
        vertical.sort()
        ans = []
        for col, nodes in vertical:
            nodes.sort()
            temp = [x[1] for x in nodes]
            ans.append(temp)

        return ans
