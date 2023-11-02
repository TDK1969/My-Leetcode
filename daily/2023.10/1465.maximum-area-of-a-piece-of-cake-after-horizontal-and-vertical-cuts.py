"""
日期: 2023-10-27
题目: 切割后面积最大的蛋糕
链接: https://leetcode-cn.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
"""

from typing import *
from collections import *
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i - 1])
        
        max_w = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i - 1])

        return (max_h * max_w) % (10 ** 9 + 7)
    

test = Solution()
print(test.maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]))