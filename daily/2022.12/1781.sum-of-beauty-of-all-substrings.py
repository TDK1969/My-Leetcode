"""
日期: 2022-12-12
题目: 所有子字符串美丽值之和
链接: https://leetcode-cn.com/problems/sum-of-beauty-of-all-substrings/
"""

from typing import *
from collections import *
class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            c = Counter()
            for j in range(i, n):
                c[s[j]] += 1
                ans += max(c.values()) - min(c.values())
        return ans

test = Solution()
print(test.beautySum("aabcb"))