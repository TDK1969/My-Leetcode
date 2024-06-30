"""
日期: 2024-04-10
题目: 用最少数量的箭引爆气球
链接: https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:[x[1], x[0]])
        ans = 0
        n = len(points)
        i = 0
        while i < n:
            j = i
            while j < n and points[j][0] <= points[i][1] <= points[j][1]:
                    j += 1
                
            ans += 1
            i = j
        return ans

print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
"""
--TESTCASE BEGIN--
TestCase 0: [[10,16],[2,8],[1,6],[7,12]]
TestCase 1: [[1,2],[3,4],[5,6],[7,8]]
TestCase 2: [[1,2],[2,3],[3,4],[4,5]]
--TESTCASE END--
""" 
