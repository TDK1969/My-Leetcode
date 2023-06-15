"""
题目: 找出数组的串联值
链接: https://leetcode-cn.com/problems/find-the-array-concatenation-value/
"""

from typing import *
from collections import *
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        i = 0
        j = n - 1

        while i < j:
            temp = int(str(nums[i]) + str(nums[j]))
            ans += temp
            i += 1
            j -= 1
        if i == j:
            ans += nums[i]

        return ans