"""
题目: 将珠子放入背包中
链接: https://leetcode-cn.com/problems/put-marbles-in-bags/
"""

from typing import *
from collections import *
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        s = []
        n = len(weights)
        for i in range(n - 1):
            s.append(weights[i] + weights[i + 1])
        s.sort()
        return sum(s[n - k:]) - sum(s[:k - 1])

test = Solution()
print(test.putMarbles(weights = [1,4,2,5,2], k = 3))