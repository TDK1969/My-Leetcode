"""
日期: 2024-11-27
题目: 交替组 II
链接: https://leetcode.cn/problems/alternating-groups-ii/
"""

from typing import *
from collections import *
from leetcode_utils import *
import bisect
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        broken_points = []
        n = len(colors)
        for i in range(n):
            if colors[i] == colors[(i + 1) % n]:
                broken_points.append(i)
        
        for i in range(n):
            if colors[i] == colors[(i + 1) % n]:
                broken_points.append(n + i)

        ans = 0
        for i in range(n):
            # 判断以i为开头，i + k - 1为结尾的组是否是交替组
            # 即需要判断[i, i + k - 2]区间内是否有broken_point
            idx = bisect.bisect_right(broken_points, i + k - 2)
            if


        
        

"""
--TESTCASE BEGIN--
TestCase 0: [0,1,0,1,0],3
TestCase 1: [0,1,0,0,1,0,1],6
TestCase 2: [1,1,0,1],4
--TESTCASE END--
""" 
