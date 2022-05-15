"""
日期: 2022-05-15
题目: 最大三角形面积
链接: https://leetcode-cn.com/problems/largest-triangle-area/
"""

from typing import *
from collections import *
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        n = len(points)

        def calc(p1: List[int], p2: List[int]) -> float:
            return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c = calc(points[i], points[j]), calc(points[i], points[k]), calc(points[j], points[k])
                    p = (a + b + c) / 2
                    try:
                        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
                        
                        if s > max_area:
                            max_area = s
                    except Exception:
                        pass
        
        return max_area

test = Solution()
print(test.largestTriangleArea([[35,-23],[-12,-48],[-34,-40],[21,-25],[-35,-44],[24,1],[16,-9],[41,4],[-36,-49],[42,-49],[-37,-20],[-35,11],[-2,-36],[18,21],[18,8],[-24,14],[-23,-11],[-8,44],[-19,-3],[0,-10],[-21,-4],[23,18],[20,11],[-42,24],[6,-19]]))