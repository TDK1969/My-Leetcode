"""
日期: 2022-06-11
题目: 将字符串翻转到单调递增
链接: https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/
"""

from typing import *
from collections import *
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        presums = []
        cnt = 0
        for bit in s:
            if bit == "1":
                cnt += 1
            presums.append(cnt)

        n = len(s)
        ans = n
        for i in range(n):
            if i == 0:
                ans = min(ans, n - 1 - (presums[-1] - presums[0]))
            elif i == n - 1:
                ans = min(ans, presums[-2])
            else:
                ans = min(ans, presums[i - 1] + (n - i - 1 - presums[-1] + presums[i]))
        return ans

test = Solution()
print(test.minFlipsMonoIncr("11011"))