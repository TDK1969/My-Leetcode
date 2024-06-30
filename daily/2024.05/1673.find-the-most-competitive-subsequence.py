"""
日期: 2024-05-24
题目: 找出最具竞争力的子序列
链接: https://leetcode.cn/problems/find-the-most-competitive-subsequence/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []
        n = len(nums)
        for i in range(n):
            while s and len(s) + n - i > k and nums[i] < s[-1]:
                s.pop()
            s.append(nums[i])
        return s[:k]
                
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []
        n = len(nums)
        for i in range(n):
            while s and len(s) + n - i > k and nums[i] < s[-1]:
                s.pop()
            if len(s) < k:
                s.append(nums[i])
        return s
                
            
print(Solution().mostCompetitive([2,4,3,3,5,4,9,6],4))

"""
--TESTCASE BEGIN--
TestCase 0: [3,5,2,6],2
TestCase 1: [2,4,3,3,5,4,9,6],4
--TESTCASE END--
""" 
