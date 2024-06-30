"""
日期: 2024-03-19
题目: IPO
链接: https://leetcode-cn.com/problems/ipo/
"""

from typing import *
from collections import *
from leetcode_utils import *
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h = []
        heapq.heapify(h)
        n = len(profits)
        t = list(zip(capital, profits))
        t.sort()

        p = 0
        ans = w
        while k:
            while p < n and ans >= t[p][0]:
                heapq.heappush(h, -t[p][1])
                p += 1

            if len(h) > 0:
                ans -= heapq.heappop(h)
            else:
                break

            k -= 1
        return ans

print(Solution().findMaximizedCapital(9,0,[1,2,3],[0,1,2]))   

"""
--TESTCASE BEGIN--
TestCase 0: 2,0,[1,2,3],[0,1,1]
TestCase 1: 3,0,[1,2,3],[0,1,2]
--TESTCASE END--
""" 
