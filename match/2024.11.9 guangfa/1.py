from typing import List
class TreeNode:
    def __init__(self, val: str, left: "TreeNode"=None, right: "TreeNode"=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binTreePaths(self , nodes: List[str], key: str) -> str:
        # write code here
        ans = []
        tree_map = dict()
        for i in range(len(nodes)):
            if nodes[i] != "#":
                tree_map[nodes[i]] = TreeNode(nodes[i])

        for i in range(len(nodes)):
            if i * 2 + 1 < len(nodes) and nodes[i * 2 + 1] != "#":
                tree_map[nodes[i]].left = tree_map[nodes[i * 2 + 1]]

            if i * 2 + 2 < len(nodes) and nodes[i * 2 + 2] != "#":
                tree_map[nodes[i]].right = tree_map[nodes[i * 2 + 2]]
        

        flag = False
        path = []

        def dfs(node: "TreeNode"):
            nonlocal flag
            path.append("/" + node.val)
            if node.val == key:
                flag = True
                ans.append("".join(path))
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            if not node.left and not node.right and flag:
                ans.append("".join(path))
            path.pop()
        
        dfs(tree_map[nodes[0]])

        if len(ans) == 2 and ans[0] == ans[1]:
            return ans[0]
        else:
            return ",".join(ans)


print(Solution().binTreePaths(["1", "2", "3", "4", "#", "#", "5"], "5"))
