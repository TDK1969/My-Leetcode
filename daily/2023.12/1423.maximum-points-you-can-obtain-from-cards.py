"""
日期: 2023-12-03
题目: 可获得的最大点数
链接: https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k <= len(cardPoints) // 2:
            ans = sum(cardPoints[:k])
            t = ans
            for i in range(k):
                t = t - cardPoints[k - 1 - i] + cardPoints[-i-1]
                ans = max(ans, t)
            return ans
        else:
            n = len(cardPoints)
            # 滑动窗口大小为 n-k
            windowSize = n - k
            # 选前 n-k 个作为初始值
            s = sum(cardPoints[:windowSize])
            minSum = s
            for i in range(windowSize, n):
                # 滑动窗口每向右移动一格，增加从右侧进入窗口的元素值，并减少从左侧离开窗口的元素值
                s += cardPoints[i] - cardPoints[i - windowSize]
                minSum = min(minSum, s)
            return sum(cardPoints) - minSum

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,4,5,6,1],3
TestCase 1: [2,2,2],2
TestCase 2: [9,7,7,9,7,7,9],7
--TESTCASE END--
""" 

print(Solution().maxScore(cardPoints = [1,79,80,1,1,1,200,1], k = 3))