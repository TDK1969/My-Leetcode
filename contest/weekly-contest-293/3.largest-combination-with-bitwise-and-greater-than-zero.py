"""
题目: 按位与结果大于零的最长组合
链接: https://leetcode-cn.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
"""

from cmath import log
from typing import *
from collections import *

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        n = 0
        t = max(candidates)
        while 1 << n <= candidates:
            n += 1 
        cnt = [0 for _ in range(n)]

        for c in candidates:
            for i in range(n):
                if c & (1 << i):
                    cnt[i] += 1
        
        return max(cnt)

