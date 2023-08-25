"""
题目: 构造最长的新字符串
链接: https://leetcode-cn.com/problems/construct-the-longest-new-string/
"""

from typing import *
from collections import *
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == 0 and y == 0:
            return z * 2
        if y == 0:
            return (z + min(x, 1)) * 2
        if x == 0:
            return( z + min(y, 1)) * 2
        if z == 0:
            return (min(x, y) * 2 + int(x != y)) * 4
        if x * y * z != 0:
            return (min(x, y) * 2 + int(x != y) + z) * 2

test = Solution()
print(test.longestString(2, 5, 1))