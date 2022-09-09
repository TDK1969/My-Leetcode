"""
日期: 2022-07-14
题目: 子集
链接: https://leetcode-cn.com/problems/subsets/
"""

from typing import *
from collections import *
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        temp = []
        def dfs(i: int):
            for j in range(i, len(nums)):
                temp.append(nums[j])
                ans.append(temp[:])
                dfs(j + 1)
                temp.pop()
        dfs(0)
        return ans

test = Solution()
print(test.subsets([1,2,3]))
