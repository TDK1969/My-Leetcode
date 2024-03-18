"""
日期: 2024-01-19
题目: 将有序数组转换为二叉搜索树
链接: https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make_tree(s: int, e: int) -> Optional[TreeNode]:
            if s == e:
                return TreeNode(nums[s])
            if s > e:
                return None
            mid = (s + e) >> 1
            return TreeNode(nums[mid], make_tree(s, mid - 1), make_tree(mid + 1, e))
        return make_tree(0, len(nums) - 1)

show_tree(Solution().sortedArrayToBST([-10,-3,0,5,9]))


"""
--TESTCASE BEGIN--
TestCase 0: [-10,-3,0,5,9]
TestCase 1: [1,3]
--TESTCASE END--
""" 
