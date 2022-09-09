"""
日期: 2022-07-14
题目: 接雨水
链接: https://leetcode-cn.com/problems/trapping-rain-water/
"""

from typing import *
from collections import *
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0 for _ in range(n)]
        left[0] = height[0]
        right = [0 for _ in range(n)]
        right[-1] = height[-1]

        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        
        ans = 0
        for i in range(n):
            ans += max(0, min(left[i], right[i]) - height[i])

        return ans
    
    def trap(self, height: List[int]) -> int:
        # 双指针 
        # 时间复杂度: O(n)
        # 空间复杂度: O(1)

        n = len(height)
        ans = 0
        left, right = 0, n - 1
        left_max = height[left]
        right_max = height[right]

        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, height[left])
                ans += left_max - height[left] 
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1

        return ans
    
    def trap(self, height: List[int]) -> int:
        # 单调栈思路
        # 时间复杂度: O(n)
        # 空间复杂度: O(n)
        stack = [] # 栈中的值为索引而不是高度
        ans = 0
        n = len(height)
        
        for i in range(n):
            if not stack or height[stack[-1]] > height[i]:
                stack.append(i)
            else:
                while stack and height[stack[-1]] <= height[i]:
                    bottem_line = height[stack.pop()]
                    if stack:
                        ans += (min(height[stack[-1]], height[i]) - bottem_line) * (i - stack[-1] - 1)
                stack.append(i)
        return ans
                


test = Solution()
print(test.trap([4,2,0,3,2,5]))