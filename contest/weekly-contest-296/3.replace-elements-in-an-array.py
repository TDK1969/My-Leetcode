"""
题目: 替换数组中的元素
链接: https://leetcode-cn.com/problems/replace-elements-in-an-array/
"""

from typing import *
from collections import *

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {value:index for index, value in enumerate(nums)}
        for old_num, new_num in operations:
            index = d[old_num]
            d[old_num] = -1
            d[new_num] = index
        
        ans = [0 for _ in range(len(nums))]
        for num, index in d.items():
            if index != -1:
                ans[index] = num
        return ans