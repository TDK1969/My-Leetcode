"""
日期: 2023-10-25
题目: 求一个整数的惩罚数
链接: https://leetcode-cn.com/problems/find-the-punishment-number-of-an-integer/
"""

from typing import *
from collections import *
import bisect
class Solution:
    def punishmentNumber(self, n: int) -> int:
        """
        p = []
        for i in range(1, 1000):
            digits = str(i ** 2)
            def f(start: int, pre: int, target: int) -> bool:
                if start == len(digits):
                    if pre == target:
                        return True
                for i in range(start + 1, len(digits) + 1):
                    if f(i, pre + int(digits[start:i]), target):
                        return True
                return False
            
            
            if f(0, 0, i):
                p.append(i)

        print(p)
        """
        p = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
        index = bisect.bisect_right(p, n)
        ans = sum([i ** 2 for i in p[:index]])
        return ans

test = Solution()
print(test.punishmentNumber(1000))
                
