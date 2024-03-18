"""
日期: 2022-07-14
题目: 盛最多水的容器
链接: https://leetcode-cn.com/problems/container-with-most-water/
"""

from typing import *
from collections import *
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            ans = max(ans, min(height[left], height[right]) * (right - left))
        return ans
