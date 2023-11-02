"""
日期: 2023-09-29
题目: 种花问题
链接: https://leetcode-cn.com/problems/can-place-flowers/
"""

from typing import *
from collections import *
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        pre = 0
        for i, val in enumerate([1, 0] + flowerbed + [0, 1]):
            if val == 1:
                cnt += max((i - pre) // 2 - 1, 0)
                pre = i
        
        return n <= cnt

test = Solution()
print(test.canPlaceFlowers([1,0,0,0,1,0,0], 2))