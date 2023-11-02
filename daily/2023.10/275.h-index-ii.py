"""
日期: 2023-10-30
题目: H 指数 II
链接: https://leetcode-cn.com/problems/h-index-ii/
"""

from typing import *
from collections import *
import bisect

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ans = 0
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if citations[n - mid] >= mid:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans