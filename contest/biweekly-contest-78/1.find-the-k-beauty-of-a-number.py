"""
题目: 找到一个数字的 K 美丽值
链接: https://leetcode-cn.com/problems/find-the-k-beauty-of-a-number/
"""

from typing import *
from collections import *
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0

        s = str(num)
        n = len(s)
        for i in range(n - k + 1):
            temp = int(s[i:i + k])
            if temp == 0:
                continue
            if num % temp == 0:
                ans += 1
        return ans

test = Solution()
print(test.divisorSubstrings(30003, 3))