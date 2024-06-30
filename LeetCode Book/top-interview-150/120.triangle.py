"""
日期: 2024-03-20
题目: 三角形最小路径和
链接: https://leetcode-cn.com/problems/triangle/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [float("inf") for _ in range(n)]
        dp[0] = triangle[0][0]
        for i in range(2, n + 1):
            for j in range(i - 1, 0, -1):
                dp[j] = min(dp[j], dp[j - 1]) + triangle[i - 1][j]
            dp[0] = dp[0] + triangle[i - 1][0]
        
        return min(dp)

print(Solution().minimumTotal([[2]]))

"""
--TESTCASE BEGIN--
TestCase 0: [[2],[3,4],[6,5,7],[4,1,8,3]]
TestCase 1: [[-10]]
--TESTCASE END--
""" 
