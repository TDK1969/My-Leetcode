"""
日期: 2023-11-01
题目: 最长连续序列
链接: https://leetcode-cn.com/problems/longest-consecutive-sequence/
"""

from typing import *
from collections import *
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for num in s:
            if num - 1 in s:
                continue
            i = 1
            while num + i in s:
                i += 1
            ans = max(ans, i)
        return ans

print(Solution().longestConsecutive([100,4,200,1,3,2]))