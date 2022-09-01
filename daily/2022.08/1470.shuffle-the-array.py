"""
日期: 2022-08-29
题目: 重新排列数组
链接: https://leetcode-cn.com/problems/shuffle-the-array/
"""

from typing import *
from collections import *
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans
