"""
日期: 2023-10-29
题目: H 指数
链接: https://leetcode-cn.com/problems/h-index/
"""

from typing import *
from collections import *
import bisect
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        ans = 0
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            t = bisect.bisect_left(citations, mid)
            if n - t >= mid:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        """       
        for h in range(1, n + 1):
            t = bisect.bisect_left(citations, h)
            if n - t >= h:
                ans = h
            else:
                break
        """
        return ans

print(Solution().hIndex(citations = [0]))
    
