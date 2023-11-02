"""
日期: 2023-09-01
题目: 买钢笔和铅笔的方案数
链接: https://leetcode-cn.com/problems/number-of-ways-to-buy-pens-and-pencils/
"""

from typing import *
from collections import *
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        c1, c2 = max(cost1, cost2), min(cost1, cost2)
        for i in range(total // c1 + 1):
            ans += (total - i * c1) // c2 + 1
        return ans
    
test = Solution()
print(test.waysToBuyPensPencils(total = 20, cost1 = 10, cost2 = 5))