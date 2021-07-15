from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        n = len(trees)
        leaves = {}
        for root in trees:
            if root.left:
                leaves[root.left.val] = [root, "L", False]
            if root.right:
                leaves[root.right.val] = [root, "R", False]

        for i in range(n - 1, -1, -1):
            root = trees[i]
            if root.val in leaves:
                parent_obj = leaves[root.val]
                if parent_obj[1] == "L":
                    parent_obj[0].left = root
                if parent_obj[1] == "R":
                    parent_obj[0].right = root
                del trees[i]
        if len(trees) == 1:
            self.flag = True
            def check_tree(node, l, r):
                if node.val < l or node.val > r:
                    self.flag = False
                    return
                if node.left:
                    leaves[node.left.val][2] = True
                    check_tree(node.left, l, min(r, node.val))
                if node.right:
                    leaves[node.right.val][2] = True
                    check_tree(node.right, max(l, node.val), r)
            check_tree(trees[0], -float("inf"), float("inf"))
            if self.flag:
                for leaf in leaves:
                    if not leaves[leaf][2]:
                        return None
                return trees[0]
        return None






