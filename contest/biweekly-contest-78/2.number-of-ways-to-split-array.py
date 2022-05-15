"""
题目: 分割数组的方案数
链接: https://leetcode-cn.com/problems/number-of-ways-to-split-array/
"""

from typing import *
from collections import *

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        presums = []
        temp = 0
        for num in nums:
            temp += num
            presums.append(temp)
        
        ans = 0
        for i in presums[:len(presums)]:
            if i << 1 >= presums[-1]:
                ans += 1
        return ans