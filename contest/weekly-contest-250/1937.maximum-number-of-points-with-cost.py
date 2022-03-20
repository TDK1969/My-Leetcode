from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = [[0 for y in range(n)] for x in range(m)]
