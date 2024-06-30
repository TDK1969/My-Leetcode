"""
日期: 2024-05-16
题目: 你可以工作的最大周数
链接: https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        longest = max(milestones)
        rest = sum(milestones) - longest
        if longest > rest + 1:
            return rest * 2 + 1
        else:
            return longest + rest
        


                

        

            
print(Solution().numberOfWeeks([1,2,2]))


"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3]
TestCase 1: [5,2,1]
--TESTCASE END--
""" 
