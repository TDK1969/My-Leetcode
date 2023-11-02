"""
日期: 2023-11-02
题目: 环和杆
链接: https://leetcode-cn.com/problems/rings-and-rods/
"""

from typing import *
from collections import *
class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        res = 0
        for i in range(0, n, 2):
            color, pos = {"R": 1, "G": 2, "B": 4}[rings[i]], int(rings[i + 1])
            res |= color << (pos * 3)
        
        ans = 0
        for i in range(10):
            if res & 7 == 7:
                ans += 1
            res = res >> 3
        return ans

print(Solution().countPoints("B0B6G0R6R0R6G9"))

