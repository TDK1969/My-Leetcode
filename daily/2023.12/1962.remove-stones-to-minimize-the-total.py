"""
日期: 2023-12-23
题目: 移除石子使总数最小
链接: https://leetcode-cn.com/problems/remove-stones-to-minimize-the-total/
"""

from typing import *
from collections import *
from leetcode_utils import *
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)

        for pile in piles:
            heapq.heappush(h, -pile)
        
        s = sum(piles)

        for _ in range(k):
            if s == len(piles):
                break
            temp = -heapq.heappop(h)
            remove = temp // 2
            s -= remove
            heapq.heappush(h, -(temp - remove))
        
        return s

"""
--TESTCASE BEGIN--
TestCase 0: [5,4,9],2
TestCase 1: [4,3,6,7],3
--TESTCASE END--
""" 

print(Solution().minStoneSum([4,3,6,7],3))
