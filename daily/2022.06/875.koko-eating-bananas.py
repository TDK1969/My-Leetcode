"""
日期: 2022-06-07
题目: 爱吃香蕉的珂珂
链接: https://leetcode-cn.com/problems/koko-eating-bananas/
"""

from math import ceil
from typing import *
from collections import *
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        piles.sort(reverse=True)

        def check(speed: int) -> bool:
            t = 0
            for p in piles:   
                t += ceil(p / speed)
                if t > h:
                    return False
            return True

        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l

test = Solution()
print(test.minEatingSpeed(piles = [312884470], h = 968709470))
            