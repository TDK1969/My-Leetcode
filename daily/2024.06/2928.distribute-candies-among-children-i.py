"""
日期: 2024-06-01
题目: 给小朋友们分糖果 I
链接: https://leetcode.cn/problems/distribute-candies-among-children-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(limit + 1):
            remain = n - i
            # 剩下n-i，0 ~ min(limit, remain)
            # 最小取值 max(0, remain - limit)
            # 最大取值 min(limit, remain)
            ans += max(0, min(limit, remain) - max(0, remain - limit) + 1)
        return ans

print(Solution().distributeCandies(n = 3, limit = 3))

"""
--TESTCASE BEGIN--
TestCase 0: 5,2
TestCase 1: 3,3
--TESTCASE END--
""" 
