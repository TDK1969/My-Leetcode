"""
日期: 2022-07-29
题目: 有效的正方形
链接: https://leetcode-cn.com/problems/valid-square/
"""

from typing import *
from collections import *
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p = [p1, p2, p3, p4]
        p.sort()
        p[2], p[3] = p[3], p[2]

        edge1 = (p[0][0] - p[1][0]) ** 2 + (p[0][1] - p[1][1]) ** 2
        edge2 = (p[1][0] - p[2][0]) ** 2 + (p[1][1] - p[2][1]) ** 2
        edge3 = (p[2][0] - p[3][0]) ** 2 + (p[2][1] - p[3][1]) ** 2
        edge4 = (p[3][0] - p[0][0]) ** 2 + (p[3][1] - p[0][1]) ** 2

        if edge1 == edge2 == edge3 == edge4 and (p[1][1] - p[0][1]) * (p[2][0] - p[1][0]) == (p[2][1] - p[1][1]) * (p[0][0] - p[1][0]):
            return True
        return False

test = Solution()
print(test.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))