"""
日期: 2022-08-09
题目: 逐步求和得到正数的最小值
链接: https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum/
"""

from typing import *
from collections import *
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0
        for i in nums:
            cnt += i
            ans = min(ans, cnt)
        return abs(ans) + 1
        