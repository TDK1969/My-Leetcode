"""
日期: 2023-12-28
题目: 收集巧克力
链接: https://leetcode-cn.com/problems/collecting-chocolates/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        min_cost = nums[:]
        ans = sum(min_cost)

        for i in range(1, n):
            for j in range(n):
                # 类型为(j + i) % n的巧克力成本为nums[j] + i * x
                min_cost[(j + i) % n] = min(min_cost[(j + i) % n], nums[j])
            ans = min(ans, sum(min_cost) + i * x)
        
        return ans


"""
--TESTCASE BEGIN--
TestCase 0: [20,1,15],5
TestCase 1: [1,2,3],4
--TESTCASE END--
""" 

print(Solution().minCost([1,2,3],4))
