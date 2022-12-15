"""
日期: 2022-11-23
题目: 盒子中小球的最大数量
链接: https://leetcode-cn.com/problems/maximum-number-of-balls-in-a-box/
"""

from typing import *
from collections import *
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            t = 0
            while i > 0:
                t += i % 10
                i = i // 10
            ans[t] += 1
        return max(ans.values())

test = Solution()
print(test.countBalls(5, 15))