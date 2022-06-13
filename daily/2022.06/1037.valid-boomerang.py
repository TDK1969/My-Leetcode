"""
日期: 2022-06-08
题目: 有效的回旋镖
链接: https://leetcode-cn.com/problems/valid-boomerang/
"""

from typing import *
from collections import *
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if len(set([tuple(i) for i in points])) != len(points):
            return False
        k1 = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0]) if points[1][0] != points[0][0] else float("inf")
        k2 = (points[1][1] - points[2][1]) / (points[1][0] - points[2][0]) if points[1][0] != points[2][0] else float("inf")
        return k1 != k2