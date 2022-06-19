"""
日期: 2022-06-19
题目: 出现次数最多的子树元素和
链接: https://leetcode-cn.com/problems/most-frequent-subtree-sum/
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
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.cnt = defaultdict(int)

        def dfs(root: TreeNode) -> int:
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                self.cnt[root.val + l + r] += 1
                return root.val + l + r
            else:
                return 0
        
        dfs(root)
        ans = []
        t = max(self.cnt.values())
        for i in self.cnt:
            if self.cnt[i] == t:
                ans.append(i)
        
        return ans
