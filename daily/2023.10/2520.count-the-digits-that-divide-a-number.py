"""
日期: 2023-10-26
题目: 统计能整除数字的位数
链接: https://leetcode-cn.com/problems/count-the-digits-that-divide-a-number/
"""

from typing import *
from collections import *
class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        t = num
        while t:
            if t % 10 and num % (t % 10) == 0:
                ans += 1
            t = t // 10
        return ans

test = Solution()
print(test.countDigits(10))