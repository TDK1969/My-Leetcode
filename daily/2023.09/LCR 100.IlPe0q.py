"""
日期: 2023-09-18
题目: 三角形最小路径和
链接: https://leetcode-cn.com/problems/IlPe0q/
"""

from typing import *
from collections import *
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp1 = [triangle[0][0]]
        dp2 = []

        for layer in triangle[1:]:
            dp2.append(dp1[0] + layer[0])
            
            for i in range(1, len(layer) - 1):
                dp2.append(min(dp1[i], dp1[i - 1]) + layer[i])

            dp2.append(dp1[-1] + layer[-1])

            dp1 = dp2
            dp2 = []
        return min(dp1)

test = Solution()
print(test.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))