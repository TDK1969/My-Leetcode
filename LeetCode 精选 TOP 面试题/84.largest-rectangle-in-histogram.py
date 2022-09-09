"""
日期: 2022-07-14
题目: 柱状图中最大的矩形
链接: https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
"""

from typing import *
from collections import *
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        # left_lower[i]表示下标为i的柱子左侧第一个高度比i小的下标
        left_lower = [0 for _ in range(n)]
        # right_lower[i]表示下标为i的柱子右侧第一个高度比i小的下标
        right_lower = [0 for _ in range(n)]

        # 维护单调栈,元素出栈时,栈顶即为左侧第一个较低的下标
        # 栈元素: (height, index)
        # 加入哨兵
        stack = [(-1, -1)]
        for index, height in enumerate(heights):
            while height <= stack[-1][0]:
                t = stack.pop()
                left_lower[t[1]] = stack[-1][1]
            stack.append((height, index))
        # 处理栈中剩余的内容
        while len(stack) > 1:
            t = stack.pop()
            left_lower[t[1]] = stack[-1][1]
        
        stack.pop()
        stack.append((-1, n))

        for index, height in list(enumerate(heights))[::-1]:
            while height <= stack[-1][0]:
                t = stack.pop()
                right_lower[t[1]] = stack[-1][1]
            stack.append((height, index))
        while len(stack) > 1:
            t = stack.pop()
            right_lower[t[1]] = stack[-1][1]
        
        for i, height in enumerate(heights):
            ans = max(ans, (right_lower[i] - left_lower[i] - 1) * height)

        return ans

test = Solution()
print(test.largestRectangleArea([2,1,5,6,2,3]))
