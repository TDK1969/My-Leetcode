from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        root_vals = [x.val for x in trees]

        def update_leaves(ttrees: List[TreeNode]) -> List[TreeNode]:
            leaves = []

            for tree in ttrees:
                queue = []
                queue.append(tree)

                while queue:
                    if tree.left:
                        queue.append(tree.left)
                    if tree.right:
                        queue.append(tree.right)
                    if not tree.left and not tree.right:
                        leaves.append(tree)
            return leaves
        leaves = update_leaves(trees)
        leaves_vals = [x.val for x in leaves]
        if len(leaves_vals) != len(set(leaves_vals)):
            return None

        leaves_dict = {x.val : x for x in leaves}
        leaves_vals = set(leaves_vals)
        while len(trees) > 1:
            root = None
            flag = False
            for i in range(len(trees)):
                root = trees[i]
                root_val = root.val
                if root_val in leaves_vals:
                    leave = leaves_dict[root_val]
                    leave = root
                    flag = True
                    break
            if flag:
                trees.pop(trees.index(root))
            else:
                return None

        final_tree = trees[0]

        def check(tree: TreeNode, bottom: int, top: int) -> bool:
            if tree.val <= bottom or tree.val >= top:
                return False
            return check(tree.left, bottom, tree.val) and check(tree.right, trees.val, top)

        if check(final_tree, 0, 50005):
            return final_tree
        else:
            return None



