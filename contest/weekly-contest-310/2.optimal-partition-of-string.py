"""
题目: 子字符串的最优划分
链接: https://leetcode-cn.com/problems/optimal-partition-of-string/
"""

from typing import *
from collections import *
import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        h = []
        heapq.heapify(h)

        for left, right in intervals:
            if not h:
                heapq.heappush(h, right)
                ans += 1
            else:
                t = heapq.heappop(h)
                if t < left:
                    heapq.heappush(h, right)
                else:
                    heapq.heappush(h, right)
                    heapq.heappush(h, t)
                    ans += 1
        return ans

test = Solution()
print(test.minGroups(intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]))