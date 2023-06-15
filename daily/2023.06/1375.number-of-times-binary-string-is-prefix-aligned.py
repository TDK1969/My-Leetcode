"""
日期: 2023-06-14
题目: 二进制字符串前缀一致的次数
链接: https://leetcode-cn.com/problems/number-of-times-binary-string-is-prefix-aligned/
"""

from typing import *
from collections import *
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        temp_max = 0
        visited = 0
        ans = 0

        for i in flips:
            visited += 1
            if temp_max < i:
                temp_max = i
            if visited == temp_max:
                ans += 1
    
        return ans

