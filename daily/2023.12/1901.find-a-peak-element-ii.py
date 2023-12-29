"""
日期: 2023-12-19
题目: 寻找峰值 II
链接: https://leetcode-cn.com/problems/find-a-peak-element-ii/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        l, h = 0, m - 1
        while l < h:
            mid = (l + h) >> 1
            index = mat[mid].index(max(mat[mid]))
            if mid - 1 >= 0 and mat[mid][index] < mat[mid - 1][index]:
                h = mid
                continue
            if mid + 1 < m and mat[mid][index] < mat[mid + 1][index]:
                l = mid + 1
                continue
            return [mid, index]

        
        
"""
--TESTCASE BEGIN--
TestCase 0: [[1,4],[3,2]]
TestCase 1: [[10,20,15],[21,30,14],[7,16,32]]
[[7,2,3,1,2],
 [6,5,4,2,1]]
--TESTCASE END--
""" 

print(Solution().findPeakGrid([[7,2,3,1,2],[6,5,4,2,1]]))
