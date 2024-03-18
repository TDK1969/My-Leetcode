"""
日期: 2024-01-24
题目: 美丽塔 I
链接: https://leetcode.cn/problems/beautiful-towers-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        prefix, suffix = [0] * n, [0] * n
        stack1, stack2 = [], []

        for i in range(n):
            while stack1 and maxHeights[i] < maxHeights[stack1[-1]]:
                stack1.pop()
            if stack1:
                prefix[i] = (i - stack1[-1]) * maxHeights[i] + prefix[stack1[-1]]
            else:
                prefix[i]  = (i + 1) * maxHeights[i]
            stack1.append(i)
        
        for j in range(n - 1, -1, -1):
            while stack2 and maxHeights[j] < maxHeights[stack2[-1]]:
                stack2.pop()
            if stack2:
                suffix[j] = (stack2[-1] - j) * maxHeights[j] + suffix[stack2[-1]]
            else:
                suffix[j] = (n - j) * maxHeights[j]
            stack2.append(j)
        
        ans = 0
        for i in range(n):
            ans = max(ans, prefix[i] + suffix[i] - maxHeights[i])
        return ans

print(Solution().maximumSumOfHeights([6,5,3,9,2,7]))
"""
--TESTCASE BEGIN--
TestCase 0: [5,3,4,1,1]
TestCase 1: [6,5,3,9,2,7]
TestCase 2: [3,2,5,5,2,3]
--TESTCASE END--
""" 
