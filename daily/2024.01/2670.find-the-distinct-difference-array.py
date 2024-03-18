"""
日期: 2024-01-31
题目: 找出不同元素数目差数组
链接: https://leetcode.cn/problems/find-the-distinct-difference-array/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        s = set()
        for i in range(n):
            s.add(nums[i])
            ans[i] = len(s)
        s.clear()
        for i in range(n - 1, -1, -1):
            ans[i] -= len(s)
            s.add(nums[i])
        return ans

print(Solution().distinctDifferenceArray([3,2,3,4,2]))
"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,4,5]
TestCase 1: [3,2,3,4,2]
--TESTCASE END--
""" 
