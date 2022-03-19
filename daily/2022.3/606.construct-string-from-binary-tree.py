from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ""
        def dfs(root: TreeNode):
            if dfs is not None:
                nonlocal ans
                ans += str(root.val)

                if root.left or root.right:
                    ans += "("
                    if root.left is not None:
                        dfs(root.left)
                    ans += ")"
                    if root.right is not None:
                        ans += "("
                        dfs(root.right)
                        ans += ")"
        
        if root is not None:
            dfs(root)
        
        return ans