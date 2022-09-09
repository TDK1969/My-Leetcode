"""
日期: 2022-09-05
题目: 寻找重复的子树
链接: https://leetcode-cn.com/problems/find-duplicate-subtrees/
"""

from typing import *
from collections import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        sub_tree_set = set()
        ans_set = dict()

        def dfs(r: Optional[TreeNode]) -> str:
            if not r:
                return ""
            k = "".join([str(r.val), "(", dfs(r.left), ")", "(", dfs(r.right), ")"])
            
            if k in sub_tree_set:
                ans_set[k] = r
            sub_tree_set.add(k)

            return k
        
        dfs(root)
        return list(ans_set.values())

node_tree = TreeNode(2, TreeNode(2, TreeNode(3)), TreeNode(2, TreeNode(3)))
test = Solution()
print(test.findDuplicateSubtrees(node_tree))


                
                

