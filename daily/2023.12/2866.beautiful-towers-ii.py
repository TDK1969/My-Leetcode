"""
日期: 2023-12-21
题目: 美丽塔 II
链接: https://leetcode-cn.com/problems/beautiful-towers-ii/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        left = []
        l_stack = []
        l_res = 0
        for h in maxHeights:
            k = 1
            while len(l_stack) and h < l_stack[-1][0]:
                t = l_stack.pop()
                l_res += (h - t[0]) * t[1]
                k += t[1]
            l_res += h
            left.append(l_res)
            l_stack.append((h, k))
        
        right = []
        r_stack = []
        r_res = 0
        for h in maxHeights[::-1]:
            k = 1
            while len(r_stack) and h < r_stack[-1][0]:
                t = r_stack.pop()
                r_res += (h - t[0]) * t[1]
                k += t[1]
            r_res += h
            right.append(r_res)
            r_stack.append((h, k))
        
        right.reverse()

        ans = 0
        for i in range(len(maxHeights)):
            ans = max(left[i] + right[i] - maxHeights[i], ans)
        return ans

"""
--TESTCASE BEGIN--
TestCase 0: [5,3,4,1,1]
TestCase 1: [6,5,3,9,2,7]
TestCase 2: [3,2,5,5,2,3]
--TESTCASE END--
""" 
print(Solution().maximumSumOfHeights([3,2,5,5,2,3]))