"""
题目: 出现最频繁的偶数元素
链接: https://leetcode-cn.com/problems/most-frequent-even-element/
"""

from typing import *
from collections import *
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            if num & 1 == 0:
                d[num] += 1
        ans_num = -1
        ans_count = 0
        for num, count in d.items():
            if count > ans_count:
                ans_num = num
                ans_count = count
            elif count == ans_count and num < ans_num:
                ans_num = num
        return ans_num
