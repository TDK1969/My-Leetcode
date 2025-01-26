"""
日期: 2025-01-14
题目: 超过阈值的最少操作数 I
链接: https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        q = []
        heapq.heapify(q)
        ans = 0
        for num in nums:
            heapq.heappush(q, num)
        while q[0] < k:
            heapq.heappop(q)
            ans += 1
        return ans

print(Solution().minOperations([1,1,2,4,9],9))
        

"""
--TESTCASE BEGIN--
TestCase 0: [2,11,10,1,3],10
TestCase 1: [1,1,2,4,9],1
TestCase 2: [1,1,2,4,9],9
--TESTCASE END--
""" 
