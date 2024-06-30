"""
日期: 2024-05-18
题目: 找出可整除性得分最大的整数
链接: https://leetcode.cn/problems/find-the-maximum-divisibility-score/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors = list(set(divisors))
        minDiv = max(divisors)
        maxScore = -1

        for div in divisors:
            cnt = 0
            for num in nums:
                if num % div == 0:
                    cnt += 1
            if cnt > maxScore or cnt == maxScore and div < minDiv:
                maxScore = cnt
                minDiv = div
        
        return minDiv


"""
--TESTCASE BEGIN--
TestCase 0: [4,7,9,3,9],[5,2,3]
TestCase 1: [20,14,21,10],[5,7,5]
TestCase 2: [12],[10,16]
--TESTCASE END--
""" 
