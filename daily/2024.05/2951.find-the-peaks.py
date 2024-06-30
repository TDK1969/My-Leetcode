"""
日期: 2024-05-28
题目: 找出峰值
链接: https://leetcode.cn/problems/find-the-peaks/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                ans.append(i)
        return ans

"""
--TESTCASE BEGIN--
TestCase 0: [2,4,4]
TestCase 1: [1,4,3,8,5]
--TESTCASE END--
""" 
