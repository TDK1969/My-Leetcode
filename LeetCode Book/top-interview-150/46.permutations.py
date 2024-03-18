"""
日期: 2022-07-14
题目: 全排列
链接: https://leetcode-cn.com/problems/permutations/
"""

from typing import *
from collections import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(left_nums: List[int], temp: List[int]):
            if not left_nums:
                ans.append(temp)
            else:
                for i in range(len(left_nums)):
                    dfs(left_nums[:i] + left_nums[i + 1:], temp + [left_nums[i]])
        dfs(nums, [])
        return ans