"""
题目: 不含特殊楼层的最大连续楼层数
链接: https://leetcode-cn.com/problems/maximum-consecutive-floors-without-special-floors/
"""

from typing import *
from collections import *

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans = 0
        i = bottom

        for sp in special:
            ans = max(ans, sp - i)
            i = sp + 1
        
        ans = max(ans, top - i + 1)
        return ans