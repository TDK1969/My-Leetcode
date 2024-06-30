"""
日期: 2024-05-27
题目: 找出缺失的观测数据
链接: https://leetcode.cn/problems/find-missing-observations/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        s = (m + n) * mean - sum(rolls)
        if s > 6 * n or s < n:
            return []
        k = s // n
        x = (k + 1) * n - s
        return [k] * x + [k + 1] * (n - x)


"""
--TESTCASE BEGIN--
TestCase 0: [3,2,4,3],4,2
TestCase 1: [1,5,6],3,4
TestCase 2: [1,2,3,4],6,4
--TESTCASE END--
""" 
