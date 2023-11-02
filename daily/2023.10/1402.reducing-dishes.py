"""
日期: 2023-10-22
题目: 做菜顺序
链接: https://leetcode-cn.com/problems/reducing-dishes/
"""

from typing import *
from collections import *
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        n = len(satisfaction)
        ans = pre = 0
        for i in range(n):
            pre += satisfaction[i]
            if pre < 0:
                break
            ans += pre

        return ans 

test = Solution()
print(test.maxSatisfaction([-1,-8,0,5,-9]))

