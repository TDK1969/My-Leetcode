"""
日期: 2023-11-08
题目: 最长平衡子字符串
链接: https://leetcode-cn.com/problems/find-the-longest-balanced-substring-of-a-binary-string/
"""

from typing import *
from collections import *
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        ptr = 0
        n = len(s)

        while ptr < n:
            zero_count = 0
            one_count = 0
            while ptr < n and s[ptr] != "0":
                ptr += 1

            while ptr < n and s[ptr] == "0":
                ptr += 1
                zero_count += 1
            
            while ptr < n and s[ptr] == "1" and one_count < zero_count:
                ptr += 1
                one_count += 1
            
            ans = max(ans, min(one_count, zero_count) * 2)
        
        return ans
            
print(Solution().findTheLongestBalancedSubstring("001"))  


