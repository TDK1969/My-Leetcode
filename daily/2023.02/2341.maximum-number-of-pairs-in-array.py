"""
日期: 2023-02-16
题目: 数组能形成多少数对
链接: https://leetcode-cn.com/problems/maximum-number-of-pairs-in-array/
"""

from typing import *
from collections import *
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = [0 for _ in range(101)]
        ans = 0
        for num in nums:
            count[num] += 1
            if count[num] == 2:
                ans += 1
                count[num] = 0
        return [ans, sum(count)]