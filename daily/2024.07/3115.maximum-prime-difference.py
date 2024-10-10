"""
日期: 2024-07-02
题目: 质数的最大距离
链接: https://leetcode.cn/problems/maximum-prime-difference/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = [2]
        for i in range(3, 101):
            flag = True
            for p in primes:
                if i % p == 0:
                    flag = False
                    break
            if flag:
                primes.append(i)
        
        primes = set(primes)
        min_index = max_index = -1
        for i, num in enumerate(nums):
            if num in primes:
                if min_index == -1:
                    min_index = max_index = i
                else:
                    max_index = i
        
        return max_index - min_index

print(Solution().maximumPrimeDifference([4,2,9,5,3]))

"""
--TESTCASE BEGIN--
TestCase 0: [4,2,9,5,3]
TestCase 1: [4,8,2,8]
--TESTCASE END--
""" 
