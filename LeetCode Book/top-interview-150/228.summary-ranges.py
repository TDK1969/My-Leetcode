"""
日期: 2024-03-08
题目: 汇总区间
链接: https://leetcode-cn.com/problems/summary-ranges/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        n = len(nums)
        q = 0
        while q < n:
            p = q
            while q < n - 1 and nums[q + 1] == nums[q] + 1:
                q += 1
            
            if p == q:
                ans.append(str(nums[p]))
            else:
                ans.append(f"{nums[p]}->{nums[q]}")
            
            q += 1
        return ans

print(Solution().summaryRanges([0,2,3,4,6,8,9]))
"""
--TESTCASE BEGIN--
TestCase 0: [0,1,2,4,5,7]
TestCase 1: [0,2,3,4,6,8,9]
--TESTCASE END--
""" 
