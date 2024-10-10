"""
日期: 2024-07-08
题目: 寻找数组的中心下标
链接: https://leetcode.cn/problems/find-pivot-index/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        pres = [0]
        for num in nums:
            total += num
            pres.append(pres[-1] + num)
        
        pres.append(total)
        ans = -1
        for i in range(0, len(nums)):
            if pres[i] == total - pres[i + 1]:
                ans = i
                break
        return ans


"""
--TESTCASE BEGIN--
TestCase 0: [1,7,3,6,5,6]
TestCase 1: [1,2,3]
TestCase 2: [2,1,-1]
--TESTCASE END--
""" 
