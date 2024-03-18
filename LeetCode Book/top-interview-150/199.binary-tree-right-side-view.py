"""
日期: 2023-11-16
题目: 二叉树的右视图
链接: https://leetcode-cn.com/problems/binary-tree-right-side-view/
"""

from typing import *
from collections import *
from leetcode_utils import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        nxt = deque()
        nxt.append(root)
        cur = deque()

        while nxt:
            ans.append(nxt[-1].val)
            cur, nxt = nxt, deque()
            while cur:
                t = cur.popleft()
                nxt.append(t.left) if t.left else None
                nxt.append(t.right) if t.right else None
        
        return ans


"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,None,5,None,4]
TestCase 1: [1,None,3]
TestCase 2: []
--TESTCASE END--
""" 

print(Solution().rightSideView(create_tree([1,2,3,None,5,None,4])))