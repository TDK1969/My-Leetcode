"""
日期: 2022-07-14
题目: x 的平方根 
链接: https://leetcode-cn.com/problems/sqrtx/
"""

from typing import *
from collections import *
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0
        while left <= right:
            mid = (left + right) >> 1
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
    
test = Solution()
print(test.mySqrt(15))