"""
题目: 猴子碰撞的方法数
链接: https://leetcode-cn.com/problems/count-collisions-of-monkeys-on-a-polygon/
"""

from typing import *
from collections import *
class Solution:
    def monkeyMove(self, n: int) -> int:
        # 2 ^ n - 2
        a = 2
        ans = 1
        mod = 10 ** 9 + 7
        while n != 0:
            if n & 1:
                ans = (ans * a) % mod
            n >>= 1
            a = (a * a) % mod
        return (ans - 2) % mod

test = Solution()
print(test.monkeyMove(4))