"""
日期: 2024-03-10
题目: 直线上最多的点数
链接: https://leetcode-cn.com/problems/max-points-on-a-line/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxPoints(self, points):
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        
        n, ans = len(points), 1
        for i in range(n):
            mapping = {}
            maxv = 0
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                a, b = x1 - x2, y1 - y2
                k = gcd(a, b)
                key = str(a // k) + "_" + str(b // k)
                mapping[key] = mapping.get(key, 0) + 1
                maxv = max(maxv, mapping[key])
                ans = max(ans, maxv + 1)    
        return ans

print(Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

"""
--TESTCASE BEGIN--
TestCase 0: [[1,1],[2,2],[3,3]]
TestCase 1: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
--TESTCASE END--
""" 
